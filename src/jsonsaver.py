import json
from typing import List, Dict
from src.abstract_classes import Saver

class JSONSaver(Saver):
    def save_data(self, data: List[Dict], filename: str = 'vacancies.json') -> None:
        """
        Сохраняет данные в файл в формате JSON.

        Аргументы:
        data (List[Dict]): Список данных для сохранения.
        filename (str): Имя файла для сохранения (по умолчанию 'vacancies.json').
        """
        try:
            with open(f'{filename}', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f'Произошла ошибка при сохранении данных: {str(e)}')

    def get_data(self, file: str = 'vacancies.json') -> List[Dict]:
        """
        Получает данные из файла в формате JSON.

        Аргументы:
        file (str): Имя файла для загрузки данных (по умолчанию 'vacancies.json').

        Возвращает:
        List[Dict]: Список данных из файла.
        """
        file_name: str = f'{file}'
        with open(file_name, 'r') as file:
            data: List[Dict] = json.load(file)
        return data

    def add_vacancy(self, data: Dict, filename: str = 'vacancies.json') -> None:
        """
        Добавляет вакансию к существующим данным в файле.

        Аргументы:
        data (Dict): Данные о вакансии для добавления.
        filename (str): Имя файла для добавления данных (по умолчанию 'vacancies.json').
        """
        vacancies = self.get_data(filename)
        vacancies.append(data)
        self.save_data(vacancies, filename)

    def delete_vacancy(self, data: Dict, filename: str = 'vacancies.json') -> None:
        """
        Удаляет вакансию из существующих данных в файле.

        Аргументы:
        data (Dict): Данные о вакансии для удаления.
        filename (str): Имя файла для удаления данных (по умолчанию 'vacancies.json').
        """
        vacancies = self.get_data(filename)
        if data in vacancies:
            vacancies.remove(data)
        self.save_data(vacancies, filename)
