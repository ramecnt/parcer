import requests
from src.implemented import convert_currency, is_supported_currency
from src.abstract_classes import JobAPI
from src.vacancies import Vacancy
from src.jsonsaver import JSONSaver


class HeadHunterAPI(JobAPI):
    def __init__(self):
        self._search_request: str = None  # Запрос поиска
        self._vacancies: list = None  # Список вакансий
        self._top_vacancies: list = None  # Список лучших вакансий
        self._args: dict = {
            'only_with_salary': 'true'
        }

    def _better_salary(self) -> None:
        """Обновляет данные о зарплате в вакансиях."""
        for i in self._vacancies:
            if i['salary']['currency'] == "RUR":
                i['salary']['currency'] = "RUB"
            if not i['salary']['from']:
                i['salary']['from'] = i['salary']['to']
            if not i['salary']['to']:
                i['salary']['to'] = i['salary']['from']

    def _vacancies_salary(self, currency: str) -> None:
        """Преобразует зарплату в указанную валюту."""
        self._better_salary()
        for i in self._vacancies:
            if i['salary']['currency'] != currency:
                if is_supported_currency(i['salary']['currency']):
                    i['salary']['from'] = convert_currency(i['salary']['from'], i['salary']['currency'], currency)
                    i['salary']['to'] = convert_currency(i['salary']['to'], i['salary']['currency'], currency)
                    i['salary']['currency'] = currency

    def _better_vacancies(self):
        """Преобразовывает вакансии в удобный для пользователя вид"""
        vacancies = []
        for i in self._vacancies:
            v = Vacancy(i['name'], i['url'], i['snippet']['responsibility'], i['salary']['from'],
                        i['salary']['to'],
                        i['employer']['name'])
            vacancies.append(v.get_vacancy())
        self._vacancies = vacancies

    def get_vacancies(self, search_request: str, currency: str = "RUB", better_vacancies: bool = True) -> None:
        """Получает вакансии по заданному запросу."""
        if not is_supported_currency(currency):
            print("Не поддерживаемая валюта")
        self._search_request = search_request
        self._args['text'] = self._search_request
        self._vacancies = requests.get("https://api.hh.ru/vacancies", params=self._args).json()['items']
        self._vacancies_salary(currency)
        self._better_vacancies()

    def get_top_vacancies(self, search_request: str, currency: str = "RUB", amount: int = 10) -> None:
        """Получает топ вакансий по заданному запросу."""
        self.get_vacancies(search_request, currency)
        temp = self._vacancies
        temp.sort(key=lambda x: x['salary_from'], reverse=True)
        self._top_vacancies = temp[:amount]

    def save_vacancies(self, flag: bool = False, filename: str = './data/vacancies.json') -> None:
        """Сохраняет вакансии в файл."""
        saver = JSONSaver()
        if flag:
            data = self._top_vacancies
        else:
            data = self._vacancies
        saver.save_data(data, filename)

    @property
    def vacancies(self) -> list:
        """Возвращает список вакансий."""
        return self._vacancies

    @property
    def top_vacancies(self) -> list:
        """Возвращает список лучших вакансий."""
        return self._top_vacancies

