import json
from abc import ABC, abstractmethod
from json import JSONDecodeError
from typing import Any

from config import PATH_DATA
from src.vacancies import Vacancy


class BaseFile(ABC):
    """Абстрактный класс для взаимодействия с файлами."""

    @abstractmethod
    def add_vacancy(self, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод для добавления вакансий в файл."""

        pass

    @abstractmethod
    def get_vacancy(self) -> Any:
        """Абстрактный метод получения данных из файла по указанным критериям."""

        pass

    @abstractmethod
    def delete_vacancy(self, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод для удаления вакансий из файла."""

        pass


class JSONSaver(BaseFile):
    """Класс для работы с JSON-файлами."""

    def __init__(self, file_name: str = "vacancies.json") -> None:
        """Метод для инициализации экземпляра класса для работы с JSON-файлами."""

        self.__file_name = file_name

    def read_json(self) -> Any:
        """Метод для чтения Json-файла."""

        try:
            with open(PATH_DATA / self.__file_name, "r", encoding="utf-8") as json_file:
                vacancies_list = json.load(json_file)
        except (FileNotFoundError, JSONDecodeError):
            vacancies_list = []
        return vacancies_list

    def add_vacancy(self, vacancies: list[dict]) -> None:
        """Метод для добавления вакансий в файл."""

        vacancies_list = self.read_json()

        new_vacancies = []
        if len(vacancies_list) > 0:
            for vacancy in vacancies:
                if vacancy not in vacancies_list:
                    new_vacancies.append(vacancy)
        else:
            new_vacancies.extend(vacancies)

        with open(PATH_DATA / self.__file_name, "a", encoding="utf-8") as json_file:
            json.dump(new_vacancies, json_file, ensure_ascii=False, indent=4)

    def get_vacancy(self) -> list:
        """Метод получения данных из файла по указанным критериям."""

        vacancies_list = self.read_json()
        vacancies = []
        if len(vacancies_list) > 0:
            for vacancy in vacancies_list:
                vacancies.append(Vacancy(**vacancy))
        return vacancies

    def delete_vacancy(self, vacancy: Any) -> None:
        """Метод для удаления вакансий из файла."""

        vacancies_list = self.read_json()
        if vacancy in vacancies_list:
            vacancies_list.remove(vacancy)
            with open(PATH_DATA / self.__file_name, "w", encoding="utf-8") as json_file:
                json.dump(vacancies_list, json_file, ensure_ascii=False, indent=4)
