import json
from unittest.mock import mock_open, patch

from requests import JSONDecodeError

from src.file_interaction import JSONSaver


# Проверка успешного чтения JSON-файла
@patch("builtins.open", new_callable=mock_open)
@patch("json.load")
def test_read_json_success(mock_load, mock_open, hh_vacancies):
    mock_open.return_value.read.return_value = json.dumps(hh_vacancies)
    mock_load.return_value = hh_vacancies
    json_saver = JSONSaver("test_file.json")
    result = json_saver.read_json()
    assert result == hh_vacancies


# Проверка чтения, если JSON-файл пустой
@patch("builtins.open")
@patch("json.load", side_effect=JSONDecodeError("Expecting value", "", 0))
def test_read_json_no_data(mock_load, mock_open):
    json_saver = JSONSaver("test_file.json")
    result = json_saver.read_json()
    assert result == []


# Проверка чтения, если JSON-файл не найден
@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_json_no_file(mock_open):
    json_saver = JSONSaver("test_file.json")
    result = json_saver.read_json()
    assert result == []


# Проверка получения списка вакансий из JSON-файла
@patch("builtins.open", new_callable=mock_open)
@patch("json.load")
def test_get_vacancy(mock_load, mock_open, hh_vacancies, vacancy_1, vacancy_6, vacancy_7):
    output_list = [vacancy_1, vacancy_6, vacancy_7]
    mock_open.return_value.read.return_value = json.dumps(hh_vacancies)
    mock_load.return_value = hh_vacancies
    json_saver = JSONSaver("test_file.json")
    result = json_saver.get_vacancy()
    assert len(result) == len(output_list)
