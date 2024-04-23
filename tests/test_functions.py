import pytest

from src.masks import mask_card_number, mask_account_number
from src.widget import convert_date_, number_or_account
from src.processing import filter_state, sort_by_date


def mask_card_number_test():
    assert mask_card_number('Visa Platinum 7000792289606361') == 'Visa Platinum 7000 79** **** 6361'
    assert mask_card_number('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'


@pytest.fixture
def test():
    return 'Счет **4305'


def test_with_fixture(test):
     assert test == mask_account_number('Счет 73654108430135874305') == number_or_account('Счет 73654108430135874305')


def mask_account_number_test():
    assert mask_account_number('Счет 64686473678894779589') == 'Счет **9589'


def convert_date_test_():
    assert convert_date_('2018-07-11T02:26:18.671407') == '11.07.2018'


data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.mark.parametrize("input_data, expected_result", [
    (data, [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]), ])
def test_filter_state(input_data, expected_result):
    assert filter_state(input_data) == expected_result


def sort_by_date_test():
    assert sort_by_date(data) == data
