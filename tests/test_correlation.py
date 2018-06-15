import pytest
from my_math_module import my_math_module as mmm

numbers = [[186, 15],
           [699, 69.9],
           [132, 6.5],
           [272, 22.4],
           [291, 28.4],
           [331, 65.9],
           [199, 19.4],
           [1890, 189.7],
           [788, 38.8],
           [1601, 138.2],
           ]

def test_CT10():
    assert mmm.caculate_corelation(numbers) > 0.9558

def test_CT11():
    assert mmm.caculate_corelation(numbers) < 0.9560

def test_CT12():
    try:
        mmm.caculate_corelation([])
        assert False
    except:
        assert True