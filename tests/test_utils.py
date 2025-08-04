from src.utils import filter_vacancies_by_salary, print_vacancies, top_vacancies


# Поверка вывода ТОПа вакансий по зарплате
def test_top_vacancies(vacancy_1, vacancy_6, vacancy_7):
    input_list = [vacancy_1, vacancy_6, vacancy_7]
    output_list = [vacancy_7, vacancy_6]
    assert top_vacancies(input_list, 2) == output_list


# Поверка фильтрации вакансий по зарплате
def test_filter_vacancies_by_salary(vacancy_1, vacancy_6, vacancy_7):
    input_list = [vacancy_1, vacancy_6, vacancy_7]
    output_list = [vacancy_6, vacancy_7]
    assert filter_vacancies_by_salary(input_list, 100000) == output_list


# Поверка вывода вакансий в консоль
def test_print_vacancies(vacancy_1, vacancy_6, capsys):
    input_list = [vacancy_1, vacancy_6]
    print_vacancies(input_list)
    message = capsys.readouterr()
    assert message.out.strip() == (
        "№1\n"
        'Вакансия на должность "QA тестировщик".\n'
        "Зарплата от 90000 до 180000 руб.\n"
        "Требования: Опыт тестирования REST/GraphQL API...\n"
        "Подробнее https://hh.ru/vacancy/123246166\n"
        "--------------------\n"
        "\n"
        "№2\n"
        'Вакансия на должность "Junior Python Backend Developer".\n'
        "Зарплата 120000 руб.\n"
        "Требования: Уверенное знание Python...\n"
        "Подробнее https://hh.ru/vacancy/123116250\n"
        "--------------------"
    )


# Поверка вывода вакансий в консоль, если список вакансий пуст
def test_print_vacancies_empty(capsys):
    input_list = []
    print_vacancies(input_list)
    message = capsys.readouterr()
    assert message.out.strip() == "Список вакансий пуст."
