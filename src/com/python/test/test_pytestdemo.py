'''
Created on 07-Jun-2018

@author: pratyusk
'''
import pytest

flag = 120


# content of test_sample.py
def func(x):
    return x + 2


def test_answer():
    assert func(3) == 5

    
def test_answer1():
    assert func(3) == 4

    
def test_answer2():
    assert func(3) == 5

    
def test_answer3():
    assert func(3) == 5

    
def test_answer4():
    assert func(3) == 5

y = 2
@pytest.fixture   
def initfunc():
    if y==2:
        print ("function initialization is Done", y)
    y = +1
    assert y == 3


# Run using pytest -m ans
# Run both foo and ans using pytest -m "foo or ans"
@pytest.mark.ans    
@pytest.mark.test_id(1234)    
@pytest.mark.parametrize("a", [2, 4, 6, 7])
def test_answer5(a, initfunc):
    assert a % 2 + flag == 120


# Run using pytest -m foo
@pytest.mark.foo
@pytest.mark.parametrize(("n", "expected"), [
    (1, 2),
    (2, 4)
])
def test_increment(n, expected):
    assert n + 1 == expected
    
