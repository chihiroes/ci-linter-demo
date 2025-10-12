from calculator import add, subtract
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
""""加法测试"""


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_mixed_numbers():
    assert add(5, -3) == 2


def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, -3) == -3


def test_add_float_numbers():
    assert add(1.5, 2.5) == 4.0


def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
"""减法测试"""


def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2


def test_subtract_negative_numbers():
    assert subtract(-1, -1) == 0


def test_subtract_mixed_numbers():
    assert subtract(5, -3) == 8


def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(5, 0) == 5
