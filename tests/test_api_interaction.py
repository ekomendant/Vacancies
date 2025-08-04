from unittest.mock import patch

from requests import Response

from src.api_interaction import HeadHunterAPI, HeadHunterRate


# Проверка успешного подключения к API, количество на страницу не более 100
@patch("requests.get")
def test_hhru_api_connect_1(mock_get):
    hh = HeadHunterAPI()
    mock_get.return_value = Response()
    mock_get.return_value.status_code = 200
    hh._BaseAPI__connect("Python", 3, 0)


# Проверка успешного подключения к API, количество на страницу более 100
@patch("requests.get")
def test_hhru_api_connect_2(mock_get):
    hh = HeadHunterAPI()
    mock_get.return_value = Response()
    mock_get.return_value.status_code = 200
    hh._BaseAPI__connect("Python", 101, 0)


# Проверка успешного получения вакансий с одной страницы
@patch("requests.get")
def test_hhru_get_vacancies_1(mock_get, api_response, hh_vacancies):
    hh = HeadHunterAPI()
    mock_get.return_value.json.return_value = api_response
    mock_get.return_value.status_code = 200
    assert hh.get_vacancies("Python", 3, 0) == hh_vacancies


# Проверка успешного получения вакансий с одной страницы
@patch("requests.get")
def test_hhru_get_vacancies_2(mock_get, api_response_2, hh_vacancies_2):
    hh = HeadHunterAPI()
    mock_get.return_value.json.return_value = api_response_2
    mock_get.return_value.status_code = 200
    assert hh.get_vacancies("Python", 1, 1) == hh_vacancies_2


# Проверка успешного подключения к API со справочниками для получения курса валют
@patch("requests.get")
def test_hhru_get_rate(mock_get):
    hh_rate = HeadHunterRate()
    mock_get.return_value.json.return_value = {"currency": [{"code": "EUR", "rate": 0.015982}]}
    mock_get.return_value.status_code = 200
    assert hh_rate.get_rate("EUR") == 0.015982
