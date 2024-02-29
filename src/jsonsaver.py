import json

from src.abstract_classes import Saver


class JSONSaver(Saver):
    def save_data(self, data: list, filename='vacancies.json') -> None:
        try:
            with open(f'{filename}', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except Exception as e:
            print(f'Произошла ошибка при сохранении данных: {str(e)}')

    def get_data(self, file='vacancies.json') -> list:
        file_name: str = f'{file}'
        with open(file_name, 'r') as file:
            data: list = json.load(file)
        return data

    def add_vacancy(self, data: dict, filename='vacancies.json'):
        vacancies = self.get_data(filename)
        vacancies.append(data)
        self.save_data(vacancies, filename)

    def delete_vacancy(self, data: dict, filename='vacancies.json'):
        vacancies = self.get_data(filename)
        if data in vacancies:
            vacancies.remove(data)
        self.save_data(vacancies, filename)
