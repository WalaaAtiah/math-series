import pytest
from series.series import fibonacci_iteration as fib


def test_zero():
    actual=fib(0)
    expected=0
    assert actual == expected

def test_one():
    actual=fib(1)
    expected=1
    assert actual == expected

def test_two():
    actual=fib(2)
    expected=1
    assert actual == expected

def test_three():
    actual=fib(3)
    expected=2
    assert actual == expected

def test_four():
    actual=fib(4)
    expected=3
    assert actual == expected

def test_five():
    actual=fib(5)
    expected=5
    assert actual == expected
# if the user add negative num return "you should add positive number"
def test_negative():
    actual=fib(-5)
    expected="you should enter positive number"
    assert actual == expected
# # if the user add string return "you should add positive number"
def test_string():
    actual=fib("5")
    expected="you should enter positive number"
    assert actual == expected