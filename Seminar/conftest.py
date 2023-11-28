import pytest


@pytest.fixture()
def good_word():
    return " Собака"

@pytest.fixture()
def bad_word():
    return "Сабака"