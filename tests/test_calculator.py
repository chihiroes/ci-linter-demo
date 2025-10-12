import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import add


def test_add_positive_numbers():
    """测试正常情况：正数相加"""
    assert add(2, 3) == 5


def test_add_negative_numbers():
    """测试边界情况：负数相加"""
    assert add(-1, -1) == -2


def test_add_mixed_numbers():
    """测试边界情况：正负数混合"""
    assert add(5, -3) == 2


def test_add_zero():
    """测试边界情况：包含零"""
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, -3) == -3


def test_add_float_numbers():
    """测试浮点数相加"""
    assert add(1.5, 2.5) == 4.0


def test_add_large_numbers():
    """测试大数相加"""
    assert add(1000000, 2000000) == 3000000


def test_subtract_positive_numbers():
    """测试正数相减"""
    assert subtract(5, 3) == 2


def test_subtract_negative_numbers():
    """测试负数相减"""
    assert subtract(-1, -1) == 0


def test_subtract_mixed_numbers():
    """测试正负数混合相减"""
    assert subtract(5, -3) == 8


def test_subtract_zero():
    """测试包含零的相减"""
    assert subtract(0, 0) == 0
    assert subtract(5, 0) == 5