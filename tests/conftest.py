import pytest

from src.vacancies import Vacancy


@pytest.fixture
def api_response():
    return {
        "items": [
            {
                "name": "QA тестировщик",
                "alternate_url": "https://hh.ru/vacancy/123246166",
                "salary": {"from": 90000, "to": 180000, "currency": "RUR", "gross": False},
                "snippet": {"requirement": "Опыт тестирования REST/GraphQL API..."},
            },
            {
                "name": "Junior Python Backend Developer",
                "alternate_url": "https://hh.ru/vacancy/123116250",
                "salary": {"from": None, "to": 120000, "currency": "RUR", "gross": False},
                "snippet": {"requirement": "Уверенное знание Python..."},
            },
            {
                "name": "Backend-разработчик",
                "alternate_url": "https://hh.ru/vacancy/123268248",
                "salary": {"from": 2000, "to": None, "currency": "USD", "gross": False},
                "snippet": {"requirement": "Понимание A/B‑тестирования и построения воронок через трекеры..."},
            },
        ]
    }


@pytest.fixture
def hh_vacancies():
    return [
        {
            "name": "QA тестировщик",
            "url": "https://hh.ru/vacancy/123246166",
            "salary": {"from": 90000, "to": 180000, "currency": "RUR", "gross": False},
            "requirement": "Опыт тестирования REST/GraphQL API...",
        },
        {
            "name": "Junior Python Backend Developer",
            "url": "https://hh.ru/vacancy/123116250",
            "salary": {"from": None, "to": 120000, "currency": "RUR", "gross": False},
            "requirement": "Уверенное знание Python...",
        },
        {
            "name": "Backend-разработчик",
            "url": "https://hh.ru/vacancy/123268248",
            "salary": {"from": 2000, "to": None, "currency": "USD", "gross": False},
            "requirement": "Понимание A/B‑тестирования и построения воронок через трекеры...",
        },
    ]


@pytest.fixture
def api_response_2():
    return {
        "items": [
            {
                "name": "QA тестировщик",
                "alternate_url": "https://hh.ru/vacancy/123246166",
                "salary": {"from": 90000, "to": 180000, "currency": "RUR", "gross": False},
                "snippet": {"requirement": "Опыт тестирования REST/GraphQL API..."},
            },
        ]
    }


@pytest.fixture
def hh_vacancies_2():
    return [
        {
            "name": "QA тестировщик",
            "url": "https://hh.ru/vacancy/123246166",
            "salary": {"from": 90000, "to": 180000, "currency": "RUR", "gross": False},
            "requirement": "Опыт тестирования REST/GraphQL API...",
        },
        {
            "name": "QA тестировщик",
            "url": "https://hh.ru/vacancy/123246166",
            "salary": {"from": 90000, "to": 180000, "currency": "RUR", "gross": False},
            "requirement": "Опыт тестирования REST/GraphQL API...",
        },
    ]


@pytest.fixture
def vacancy_1():
    return Vacancy(
        "QA тестировщик",
        "https://hh.ru/vacancy/123246166",
        {"from": 90000, "to": 180000, "currency": "RUR", "gross": False},
        "Опыт тестирования REST/GraphQL API...",
    )


@pytest.fixture
def vacancy_2():
    return Vacancy(
        "QA тестировщик",
        "https://hh.ru/vacancy/123246166",
        {"currency": "RUR", "gross": False},
        "Опыт тестирования REST/GraphQL API...",
    )


@pytest.fixture
def vacancy_3():
    return Vacancy(
        "QA тестировщик",
        "https://hh.ru/vacancy/123246166",
        {"to": 180000, "currency": "RUR", "gross": False},
        "Опыт тестирования REST/GraphQL API...",
    )


@pytest.fixture
def vacancy_4():
    return Vacancy(
        "QA тестировщик",
        "https://hh.ru/vacancy/123246166",
        {"from": 90000, "currency": "RUR", "gross": False},
        "Опыт тестирования REST/GraphQL API...",
    )


@pytest.fixture
def vacancy_5():
    return Vacancy(
        "QA тестировщик",
        "https://hh.ru/vacancy/123246166",
        20,
        "Опыт тестирования REST/GraphQL API...",
    )


@pytest.fixture
def vacancy_6():
    return Vacancy(
        "Junior Python Backend Developer",
        "https://hh.ru/vacancy/123116250",
        {"from": None, "to": 120000, "currency": "RUR", "gross": False},
        "Уверенное знание Python...",
    )


@pytest.fixture
def vacancy_7():
    return Vacancy(
        "Backend-разработчик",
        "https://hh.ru/vacancy/123268248",
        {"from": 2000, "to": None, "currency": "USD", "gross": False},
        "Понимание A/B‑тестирования и построения воронок через трекеры...",
    )


@pytest.fixture
def hh_vacancies_3():
    return [
        {
            "name": "Тестировщик ПО",
            "url": "https://hh.ru/vacancy/123159668",
            "salary": {"from": 140000, "to": 170000, "currency": "RUR", "gross": False},
            "requirement": "Уверенное знание Linux...",
        },
    ]
