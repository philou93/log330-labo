import pytest
from my_math_module import my_math_module as mmm


numbers = [[186, 15],
            [699, 69],
            [132, 6],
            [272, 22],
            [291, 28],
            [331, 65],
            [199, 19],
            [1890, 189],
            [788, 38],
            [1601, 138],
           ]

def test_CT13():
    assert mmm.calculate_slope(numbers) > 1.72792


def test_CT14():
    assert mmm.calculate_slope(numbers) < 1.72794


def test_CT15():
    try:
        mmm.calculate_slope([])
        assert False
    except:
        assert True
