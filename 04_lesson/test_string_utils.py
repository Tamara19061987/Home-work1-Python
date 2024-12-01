from typing import Literal
from unittest import result
import pytest

from string_utils import StringUtils

utils = StringUtils()


def test_capitalise():
    # positive
    assert utils.capitalize('skypro') == 'Skypro'
    assert utils.capitalize('hello world') == 'Hello world'
    assert utils.capitalize('123') == '123'
    # negative
    assert utils.capitalize('') == ''
    assert utils.capitalize(' ') == ' '
    assert utils.capitalize('12345тест') == '12345тест'


def test_trim():

    # positive
    assert utils.trim(' skypro') == 'skypro'
    assert utils.trim(' 123456') == '123456'
    assert utils.trim('    four') == 'four'
    assert utils.trim('') == ''
    assert utils.trim(' ') == ''

    # negative
    assert utils.trim('!skypro') == '!skypro'
    assert utils.trim('skypro') == 'skypro'
    assert utils.trim('   skypro') == 'skypro'


@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(12345) == '12345'


@pytest.mark.xfail()
def test_trim_with_spaces_output():
    assert utils.trim('  Word  ') == '  Word  '


def test_to_list():

    # positive
    # Проверка работы функции с разделителем по умолчанию
    assert utils.to_list('a,b,c,d') == ['a', 'b', 'c', 'd']
    # Проверка работы функции с пользовательским разделителем
    assert utils.to_list('1:2:3', ':') == ['1', '2', '3']

    # negative
    # Проверка работы функции с пустой строкой
    assert utils.to_list('', 'None') == []
    # Проверка работы функции с неразделимым текстом
    assert utils.to_list('abcd') == ['abcd']


@pytest.mark.xfail()
def test_to_list_with_delimeter_part_text():
    assert utils.to_list('a,b,c,d', ',a') == ['a,b,c,d', 'a']

# contains


@pytest.mark.parametrize("string, symbol, result", [
    ("pig", "i", True),
    ("plan", "n", True),
    ("собака", "б", True),
    ("who", "v", False),
    ("Extension", "g", False),
    ("12345", "4", True),
    ("abcd", "j", False),
    ("", "1", False),
    (" ", " ", True)
])
def test_contains(string: Literal['pig'] | Literal['plan'] | Literal['собака'] | Literal['who'] | Literal['Extension'] | Literal['12345'] | Literal['abcd'] | Literal[''] | Literal[' '], symbol: Literal['i'] | Literal['n'] | Literal['б'] | Literal['v'] | Literal['g'] | Literal['4'] | Literal['j'] | Literal['1'] | Literal[' '], result: bool):
    res = utils.contains(string, symbol)
    assert res == result

# delete_symbol


@pytest.mark.parametrize("string, symbol, result", [
    # positive
    ("игра", "г", "ира"),
    ("слова", "л", "сова"),
    ("12345", "345", "12"),
    ("Белый гриб", " ", "Белыйгриб"),
    # negative
    ("word", "z", "word"),
    ("12345", "", "12345"),
    ("", "k", ""),
    ("", "", ""),
])
def test_delete_symbol(string: Literal['игра'] | Literal['слова'] | Literal['12345'] | Literal['Белый гриб'] | Literal['word'] | Literal[''], symbol: Literal['г'] | Literal['л'] | Literal['345'] | Literal[' '] | Literal['z'] | Literal[''] | Literal['k'], result: Literal['ира'] | Literal['сова'] | Literal['12'] | Literal['Белыйгриб'] | Literal['word'] | Literal['12345'] | Literal['']):
    res = utils.delete_symbol(string, symbol)
    assert res == result


# start_with


@pytest.mark.parametrize("string, symbol, result", [
    # positive
    ("Future", "F", True),
    ("Future", "E", False),
    (" Apple", " ", True),
    # negative
    ("Skypro", "p", False),
    ("Питон", "М", False),
    ("", "g", False),
])
def test_start_with(string: Literal['Future'] | Literal[' Apple'] | Literal['Skypro'] | Literal['Питон'] | Literal[''], symbol: Literal['F'] | Literal['E'] | Literal[' '] | Literal['p'] | Literal['М'] | Literal['g'], result: bool):
    res = utils.starts_with(string, symbol)
    assert res == result


# end_with
#FAILED skypro_python_homeworks/lesson4/test_string_utils.py::test_end_with[student -t-True] - assert False == True
#FAILED skypro_python_homeworks/lesson4/test_string_utils.py::test_end_with[--False] - assert True == False
#FAILED skypro_python_homeworks/lesson4/test_string_utils.py::test_end_with[word--False] - assert True == False

@pytest.mark.parametrize("string, symbol, result", [
    # positive
    ("Урок", "к", True),
    ("skypro", "s", False),
    ("student", "t", True),
    # negative
    ("", "", True),
    ("", "z", False),
    ("word", "1", False),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


# is_empty

@pytest.mark.parametrize("string, result", [
    ("", True),
    (" ", True),
    ("123", False),
    # negative
    ("\n", False),  # переход на новую строку
    ("\t", False),  # табуляция
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


# list_to_string

@pytest.mark.parametrize("lst, joiner, result", [
    # positive
    ([], None, ""),
    ("1", None, "1"),
    (["1", "2", "3"], ",", "1,2,3"),
    (["1", "a", "True"], ",", "1,a,True"),
    (["a", "b", "c"], "-", "a-b-c"),
    # negative
    ([ "a", "b", "c"], " ", "a b c"),
    (["a", "b", "c"], "\n", "a\nb\nc"),
    (["a", "b", "c"], "+", "a+b+c"),
    ([" ", "  ", "   "], ",", " ,  ,   "),
])
def test_list_to_string(lst, joiner, result):
    if joiner is None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result

