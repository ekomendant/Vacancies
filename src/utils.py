from typing import Any

from src.api_interaction import HeadHunterAPI
from src.vacancies import Vacancy


def top_vacancies(vacancies: list[Vacancy], top: int = 5) -> list[Vacancy]:
    """Функция сортирует вакансии по зарплате и выводит ТОП"""

    return sorted(vacancies, reverse=True)[:top]


def filter_vacancies_by_salary(vacancies: list[Vacancy], salary: int) -> list:
    """Функция фильтрует вакансии по зарплате."""

    filtered_list = [vac for vac in vacancies if vac.get_salary >= salary]
    return filtered_list


def print_vacancies(vacancies: list[Vacancy]) -> None:
    """Функция выводит в консоль список вакансий"""

    if len(vacancies) > 0:
        for i, vacancy in enumerate(vacancies):
            print(f"\n№{i+1}" f"\n{vacancy}" "\n--------------------")
    else:
        print("\nСписок вакансий пуст.")


def search_by_key_word() -> tuple[str, Any]:
    key_word_input = input("\nВведите ключевое слово для поиска: ")
    all_vacancies = HeadHunterAPI().get_vacancies(key_word_input)
    return key_word_input, all_vacancies
