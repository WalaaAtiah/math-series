import pytest
from series.series import sum_series


#work as fibonacci series
def test_zero():
    actual=sum_series(0)
    expected=0
    assert actual == expected

def test_one():
    actual=sum_series(1)
    expected=1
    assert actual == expected

def test_two():
    actual=sum_series(2)
    expected=1
    assert actual == expected

def test_three():
    actual=sum_series(3)
    expected=2
    assert actual == expected

def test_four():
    actual=sum_series(4)
    expected=3
    assert actual == expected

def test_five():
    actual=sum_series(5)
    expected=5
    assert actual == expected
# # if the user add negative num return "you should add positive number"
def test_negative():
    actual=sum_series(-5)
    expected="you should enter positive number"
    assert actual == expected
# # if the user add string return "you should add positive number"
def test_string():
    actual=sum_series("5")
    expected="you should enter positive number"
    assert actual == expected


#work as locas series
def test_locas_zero():
    actual=sum_series(0,2,1)
    expected=2
    assert actual == expected

def test_locas_one():
    actual=sum_series(1,2,1)
    expected=1
    assert actual == expected

def test_locas_two():
    actual=sum_series(2,2,1)
    expected=3
    assert actual == expected

def test_locas_three():
    actual=sum_series(3,2,1)
    expected=4
    assert actual == expected


# # if the user add negative num return "you should add positive number"
def test_locas_negative():
    actual=sum_series(-5)
    expected="you should enter positive number"
    assert actual == expected
# # if the user add string return "you should add positive number"
def test_locas_string():
    actual=sum_series("5")
    expected="you should enter positive number"
    assert actual == expected

#work as other series  ex 3,5,8,13,21,34,55,89.......
def test_other_zero():
    actual=sum_series(0,3,5)
    expected=3
    assert actual == expected

def test_other_one():
    actual=sum_series(1,3,5)
    expected=5
    assert actual == expected

def test_other_two():
    actual=sum_series(2,3,5)
    expected=8
    assert actual == expected

def test_other_six():
    actual=sum_series(6,3,5)
    expected=55
    assert actual == expected

# # if the user add string for x,y return "you should add positive number"
def test_other_string():
    actual=sum_series(6,'3',"5")
    expected="you should enter positive number"
    assert actual == expected