import pytest
from series.series import lucas

def test_zero():
    actual=lucas(0)
    expected=2
    assert actual == expected

def test_one():
    actual=lucas(1)
    expected=1
    assert actual == expected

def test_two():
    actual=lucas(2)
    expected=3
    assert actual == expected

def test_three():
    actual=lucas(3)
    expected=4
    assert actual == expected

def test_four():
    actual=lucas(4)
    expected=7
    assert actual == expected

def test_five():
    actual=lucas(5)
    expected=11
    assert actual == expected
# if the user add negative num return "you should add positive number"
def test_negative():
    actual=lucas(-5)
    expected="you should enter positive number"
    assert actual == expected
# if the user add string return "you should add positive number"
def test_string():
    actual=lucas("5")
    expected="you should enter positive number"
    assert actual == expected

