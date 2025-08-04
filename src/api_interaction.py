from abc import ABC, abstractmethod
from typing import Any

import requests


class BaseAPI(ABC):
    """Абстрактный класс для взаимодействия с API."""

    @abstractmethod
    def _BaseAPI__connect(self, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод для подключения к API."""

        pass

    @abstractmethod
    def get_vacancies(self, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод для получения вакансий."""

        pass


class HeadHunterAPI(BaseAPI):
    """Класс для подключения к API платформы hh.ru."""

    def __init__(self) -> None:
        """Метод для инициализации экземпляра класса для работы с API сайтов с вакансиями."""

        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"page": 0, "per_page": 10, "text": "", "area": 113, "only_with_salary": True}
        self.__vacancies: list = []

    def _BaseAPI__connect(self, text: str, per_page: int = 10, page: int = 0) -> Any:
        """Метод для подключения к API."""

        self.__params["text"] = text
        if 0 < per_page <= 100:
            self.__params["per_page"] = per_page
        else:
            self.__params["per_page"] = 100
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        response.raise_for_status()
        return response

    def get_vacancies(self, text: str, per_page: int = 10, page: int = 5) -> Any:
        """Метод для получения вакансий с hh.ru в формате JSON."""

        while self.__params["page"] <= page:
            result = self._BaseAPI__connect(text, per_page=per_page).json()["items"]
            data = []
            for item in result:
                vacancy = {
                    "name": item["name"],
                    "url": item["alternate_url"],
                    "salary": item["salary"],
                    "requirement": item["snippet"]["requirement"],
                }
                data.append(vacancy)
            self.__vacancies.extend(data)
            if per_page * (self.__params["page"] + 2) <= 2000 and (self.__params["page"] + 1) <= page:
                self.__params["page"] += 1
            else:
                break
        return self.__vacancies


class HeadHunterRate:
    """Класс для подключения к API со справочниками платформы hh.ru."""

    def __init__(self) -> None:
        """Метод для инициализации экземпляра класса для работы с API со справочниками."""

        self.__url = "https://api.hh.ru/dictionaries"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"locale": "RU", "host": "hh.ru"}

    def __connect(self) -> Any:
        """Метод для подключения к API."""

        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        response.raise_for_status()
        return response

    def get_rate(self, currency_code: str) -> int | float:
        """Метод для получения курса валют"""

        rate = 1
        currency_list = self.__connect().json()["currency"]
        for currency in currency_list:
            if currency["code"] == currency_code:
                rate = currency["rate"]
                break

        return rate
