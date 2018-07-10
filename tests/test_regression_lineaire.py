import pytest
from my_math_module import my_math_module as mmm


numbers = [[130, 186],
            [650, 699],
            [99, 132],
            [150, 272],
            [128, 291],
            [302, 331],
            [95, 199],
            [945, 1890],
            [368, 788],
            [961,  1601]
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
