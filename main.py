from datetime import datetime

from src.file_interaction import JSONSaver
from src.utils import filter_vacancies_by_salary, print_vacancies, search_by_key_word, top_vacancies


def main() -> None:
    """Функция запрашивает у клиента данные для выборки вакансий и действий с ними."""

    # Приветствие и выбор параметров поиска
    print("Добро пожаловать в программу работы с вакансиями.")
    key_word_input, all_vacancies = search_by_key_word()

    while len(all_vacancies) == 0:
        zero_input = input(
            f"По ключевому слову {key_word_input.upper()} не найдено вакансий. " f"Провести новый поиск? Да / Нет: "
        )
        while zero_input.title() not in ["Да", "Нет"]:
            zero_input = input("Неверный выбор, введите Да или Нет: ")

        if zero_input.title() == "Да":
            key_word_input, all_vacancies = search_by_key_word()
        elif zero_input.title() == "Нет":
            print("Работа программы завершена.")
            return None

    # Обработка результатов поиска и вывод на экран
    if len(all_vacancies) > 0:

        now = datetime.now()
        filename = f"search_{now.strftime('%Y-%m-%d_%H-%M-%S')}.json"
        json_saver = JSONSaver(file_name=filename)
        json_saver.add_vacancy(all_vacancies)

        print(
            f"\nПо ключевому слову {key_word_input.upper()} найдено {len(all_vacancies)} вакансий. "
            f"Результат поиска сохранен в JSON-файл."
            f"\nВыберите операцию:"
            f"\n1. Показать все найденные вакансии"
            f"\n2. Показать ТОП вакансий по величине зарплаты"
            f"\n3. Показать вакансии с зарплатой выше определенного уровня"
        )

        menu_selection = input("\nВведите цифру 1, 2 или 3: ")

        while menu_selection not in ["1", "2", "3"]:
            menu_selection = input("Номер пункта выбран неверно, введите цифру 1, 2 или 3: ")

        if menu_selection == "1":
            result = json_saver.get_vacancy()
            print_vacancies(result)
        elif menu_selection == "2":
            number_input = input("Какое количество вакансий показать в ТОПе? Введите число: ")

            try:
                top_input = int(number_input)
            except ValueError:
                print("Введено некорректное число. По-умолчанию будет выведено ТОП-5 вакансий.")
                top_input = 5

            new_vacancy_list = json_saver.get_vacancy()
            result = top_vacancies(new_vacancy_list, top=top_input)
            print_vacancies(result)
        elif menu_selection == "3":
            number_input = input("Введите минимальный уровень зарплаты для фильтрации: ")

            try:
                salary_input = int(number_input)
            except ValueError:
                print("Введена некорректная сумма. По-умолчанию будут выведены вакансии с окладом от 100 000 руб.")
                salary_input = 100000

            new_vacancy_list = json_saver.get_vacancy()
            result = filter_vacancies_by_salary(new_vacancy_list, salary=salary_input)
            print_vacancies(result)

    print("Результаты поиска выведены на экран. Успешного трудоустройства!")
    return None


if __name__ == "__main__":
    main()
