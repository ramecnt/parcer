from abc import ABC, abstractmethod


class JobAPI(ABC):
    @abstractmethod
    def get_vacancies(self, *args) -> None:
        """
        Абстрактный метод для получения списка вакансий.

        Аргументы:
        *args: Произвольные аргументы, которые могут использоваться для передачи данных запроса.
        """
        pass

    @abstractmethod
    def get_top_vacancies(self, *args) -> None:
        """
        Абстрактный метод для получения списка лучших вакансий.

        Аргументы:
        *args: Произвольные аргументы, которые могут использоваться для передачи данных запроса.
        """
        pass

    @abstractmethod
    def save_vacancies(self, *args) -> None:
        pass


class Saver(ABC):
    @abstractmethod
    def save_data(self, *args) -> None:
        pass

    @abstractmethod
    def get_data(self, *args) -> None:
        pass
