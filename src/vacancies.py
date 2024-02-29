class Vacancy:
    def __init__(self, title: str, link: str, description: str, salary_from: int, salary_to: int, employer: str):
        """
        Конструктор класса Vacancy.

        Аргументы:
        title (str): Название вакансии.
        link (str): Ссылка на вакансию.
        description (str): Описание вакансии.
        salary_from (int): Нижняя граница заработной платы.
        salary_to (int): Верхняя граница заработной платы.
        employer (str): Название работодателя.
        """
        self._title: str = title
        self._link: str = link
        self._description: str = description
        self._salary_from: int = salary_from
        self._salary_to: int = salary_to
        self._employer: str = employer

    def get_vacancy(self) -> dict:
        """
        Возвращает информацию о вакансии в виде словаря.

        Возвращает:
        dict: Словарь с информацией о вакансии.
        """
        return {
            "title": self._title,
            "link": self._link,
            "description": self._description,
            "salary_from": self._salary_from,
            "salary_to": self._salary_to,
            "employer": self._employer
        }
