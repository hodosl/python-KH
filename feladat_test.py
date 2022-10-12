# egy unit test az egy függvény

from unittest import result
from feladat import *

def test_remove_all():
    # given: előkészít
    numbers = [1,2,3,1,2,3]
    # when: meghívja a tesztelendő függvényt
    result = remove_all(numbers, 2)
    # then: ellenőrzi a függvény által visszaadott adatokat
    assert result == [1,3,1,3]

def test_count_positive_numbers():
    numbers = [1,-1,1,-1,1]
    result = count_positive_numbers(numbers)
    assert result == 3