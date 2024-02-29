class Vacancy:
    def __init__(self, title: str, link: str, description: str, salary_from: int, salary_to: int, employer: str):
        self._title = title
        self._link = link
        self._description = description
        self._salary_from = salary_from
        self._salary_to = salary_to
        self._employer = employer

    def get_vacancy(self):
        return {
            "title": self._title, "link": self._link, "description": self._description,
            "salary_from": self._salary_from, "salary_to": self._salary_to, "employer": self._employer
        }



