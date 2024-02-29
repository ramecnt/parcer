import requests
from implemented import api_key
from src.abstract_classes import JobAPI
from jsonsaver import JSONSaver
from vacancies import Vacancy

class SuperJobAPI(JobAPI):
    def __init__(self):
        self._top_vacancies: list = None  # Список лучших вакансий
        self._vacancies: list = None  # Список вакансий
        self._search_request: str = None  # Поисковый запрос
        self._params: dict = {}  # Параметры запроса
        self._headers: dict = {
            'X-Api-App-Id': api_key  # Заголовки запроса с ключом API
        }

    def _better_salary(self) -> None:
        """Обработка данных о зарплате."""
        for i in self._vacancies:
            if i['payment_from'] == 0 and i['payment_to'] != 0:
                i['payment_from'] = i['payment_to']
            if i['payment_from'] != 0 and i['payment_to'] == 0:
                i['payment_to'] = i['payment_from']

    def _better_vacancies(self) -> None:
        """Преобразовывает вакансии в удобный для пользователя вид"""
        vacancies = []
        for i in self._vacancies:
            v = Vacancy(i['profession'], i['link'], i['vacancyRichText'], i['payment_from'], i['payment_to'],
                        i['firm_name'])
            vacancies.append(v.get_vacancy())
        self._vacancies = vacancies

    def get_vacancies(self, search_request: str) -> None:
        """Получает вакансии по запросу."""
        self._search_request = search_request
        self._params['keywords'] = search_request
        self._vacancies = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=self._headers,
                                       params=self._params).json()['objects']
        self._better_salary()
        self._better_vacancies()

    def get_top_vacancies(self, search_request: str, amount: int = 10) -> None:
        """Получает топ вакансий по запросу."""
        self.get_vacancies(search_request)
        temp = self._vacancies
        temp.sort(key=lambda x: x['salary_from'], reverse=True)
        self._top_vacancies = temp[:amount]

    def save_vacancies(self, flag: bool = False, filename: str = 'vacancies.json') -> None:
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
