from src.api_interaction import HeadHunterRate


class Vacancy:
    """Класс для работы с вакансиями, полученными из API-запроса."""

    __slots__ = ("name", "url", "salary", "requirement", "salary_from", "salary_to")

    def __init__(self, name: str, url: str, salary: dict, requirement: str) -> None:
        """Метод для инициализации экземпляра класса для работы с вакансиями."""

        self.name = name
        self.url = url
        self.requirement = requirement
        self.__validate_salary(salary)

    def __validate_salary(self, salary: dict) -> None:
        """Метод для валидации зарплаты по вакансии."""

        try:
            if salary.get("currency") is not None:
                currency_code = salary["currency"]
                rate = HeadHunterRate().get_rate(currency_code)
        except Exception:
            rate = 1.0

        if isinstance(salary, dict):
            if salary.get("from") is None:
                if salary.get("to") is None:
                    self.salary_from = 0
                    self.salary_to = 0
                else:
                    self.salary_from = round(salary["to"] / rate)
                    self.salary_to = round(salary["to"] / rate)
            else:
                if salary.get("to") is None:
                    self.salary_from = round(salary["from"] / rate)
                    self.salary_to = round(salary["from"] / rate)
                else:
                    self.salary_from = round(salary["from"] / rate)
                    self.salary_to = round(salary["to"] / rate)
        else:
            self.salary_from = 0
            self.salary_to = 0

    def __lt__(self, other: "Vacancy") -> bool:
        """Метод сравнения вакансий по зарплате."""

        return self.salary_from < other.salary_from

    def __str__(self) -> str:
        """Метод возвращает описание вакансии в виде строки"""

        if self.salary_from == 0 and self.salary_to == 0:
            salary = "не указана."
        elif self.salary_from < self.salary_to:
            salary = f"от {self.salary_from} до {self.salary_to} руб."
        else:
            salary = f"{self.salary_from} руб."

        return (
            f'Вакансия на должность "{self.name}".\n'
            f"Зарплата {salary}\n"
            f"Требования: {self.requirement if self.requirement else "не указаны."}\n"
            f"Подробнее {self.url}"
        )

    @property
    def get_salary(self) -> int:
        """Метод возвращает зарплату по вакансии"""

        return self.salary_from
