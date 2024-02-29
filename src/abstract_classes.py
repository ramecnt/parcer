from abc import ABC, abstractmethod


class JobAPI(ABC):
    @abstractmethod
    def get_vacancies(self, *args) -> None:
        """
        Абстрактный метод для получения списка вакансий.
        """
        pass

    @abstractmethod
    def get_top_vacancies(self, *args) -> None:
        """
        Абстрактный метод для получения списка лучших вакансий.
        """
        pass

    @abstractmethod
    def save_vacancies(self, *args) -> None:
        """
        Абстрактный метод для сохранения вакансий.
        """
        pass


class Saver(ABC):
    @abstractmethod
    def save_data(self, *args) -> None:
        """
        Абстрактный метод для сохранения данных.
        """
        pass

    @abstractmethod
    def get_data(self, *args) -> None:
        """
        Абстрактный метод для получения данных.
        """
        pass
