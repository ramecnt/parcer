from src.headhunter import HeadHunterAPI
from src.jsonsaver import JSONSaver
from src.superjob import SuperJobAPI
from src.vacancies import Vacancy
from pprint import pprint

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "Требования: опыт работы от 3 лет...", 100000,
                  150000, "Yandex")

json_saver = JSONSaver()
json_saver.add_vacancy(vacancy.get_vacancy())
json_saver.delete_vacancy(vacancy.get_vacancy())


def user_interaction():
    platform = input('Выберите платформу(superjob or hh.ru) введите ее название: \n')
    search_request = input('Введите интересующий вас поисковой запрос\n')
    if platform == 'hh.ru':
        currency = input("Введите предпочитаемую валюту\n")
        if not currency:
            currency = 'RUB'
        hh_api.get_vacancies(search_request, currency)
        pprint(hh_api.vacancies)
        amount = int(input("Введите сколько вакансий должен включать топ по зарплате\n"))
        hh_api.get_top_vacancies(search_request, currency, amount)
        pprint(hh_api.top_vacancies)
        if input("Хотите ли вы сохранить данные?\n") in ['да', 'Да', 'ДА']:
            hh_api.save_vacancies()
    else:
        superjob_api.get_vacancies(search_request)
        pprint(superjob_api.vacancies)
        amount = int(input("Введите сколько вакансий должен включать топ по зарплате\n"))
        superjob_api.get_top_vacancies(search_request, amount)
        pprint(superjob_api.top_vacancies)
        if input("Хотите ли вы сохранить данные?\n") in ['да', 'Да', 'ДА']:
            superjob_api.save_vacancies()


if __name__ == '__main__':
    user_interaction()
