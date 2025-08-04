# Проверка успешной инициализации экземпляра класса Product
def test_vacancy_init(vacancy_1):
    assert vacancy_1.name == "QA тестировщик"
    assert vacancy_1.url == "https://hh.ru/vacancy/123246166"
    assert vacancy_1.requirement == "Опыт тестирования REST/GraphQL API..."
    assert vacancy_1.get_salary == 90000
    assert vacancy_1.salary_from == 90000
    assert vacancy_1.salary_to == 180000
    assert str(vacancy_1) == (
        'Вакансия на должность "QA тестировщик".\n'
        "Зарплата от 90000 до 180000 руб.\n"
        "Требования: Опыт тестирования REST/GraphQL API...\n"
        "Подробнее https://hh.ru/vacancy/123246166"
    )


# Проверка валидации зарплаты
def test_validate_salary(vacancy_2, vacancy_3, vacancy_4, vacancy_5):
    # В ответе API не указана зарплата
    assert vacancy_2.salary_from == 0
    assert vacancy_2.salary_to == 0
    assert vacancy_2.get_salary == 0
    assert str(vacancy_2) == (
        'Вакансия на должность "QA тестировщик".\n'
        "Зарплата не указана.\n"
        "Требования: Опыт тестирования REST/GraphQL API...\n"
        "Подробнее https://hh.ru/vacancy/123246166"
    )

    # В ответе API указана только верхняя граница зарплаты
    assert vacancy_3.salary_from == 180000
    assert vacancy_3.salary_to == 180000
    assert vacancy_3.get_salary == 180000
    assert str(vacancy_3) == (
        'Вакансия на должность "QA тестировщик".\n'
        "Зарплата 180000 руб.\n"
        "Требования: Опыт тестирования REST/GraphQL API...\n"
        "Подробнее https://hh.ru/vacancy/123246166"
    )

    # В ответе API указана только нижняя граница зарплаты
    assert vacancy_4.salary_from == 90000
    assert vacancy_4.salary_to == 90000
    assert vacancy_4.get_salary == 90000
    assert str(vacancy_4) == (
        'Вакансия на должность "QA тестировщик".\n'
        "Зарплата 90000 руб.\n"
        "Требования: Опыт тестирования REST/GraphQL API...\n"
        "Подробнее https://hh.ru/vacancy/123246166"
    )

    # В ответе API ключ "salary" не содержит словаря
    assert vacancy_5.salary_from == 0
    assert vacancy_5.salary_to == 0
    assert vacancy_5.get_salary == 0
    assert str(vacancy_5) == (
        'Вакансия на должность "QA тестировщик".\n'
        "Зарплата не указана.\n"
        "Требования: Опыт тестирования REST/GraphQL API...\n"
        "Подробнее https://hh.ru/vacancy/123246166"
    )


# Проверка метода сравнения зарплат
def test_compare_salary(vacancy_1, vacancy_6):
    assert vacancy_1 < vacancy_6
