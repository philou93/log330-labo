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


def test_CT19():
    xk = 1119
    slope = mmm.calculate_slope(numbers)
    const = mmm.calculate_const(numbers, slope)
    variance = mmm.variance_with_regression(numbers, slope, const)
    std_dev = mmm.std_derivation(variance)
    student_val = 1.860
    assert mmm.calculate_interval(xk, numbers, std_dev, student_val) > 439.5455323


def test_CT20():
    xk = 1119
    slope = mmm.calculate_slope(numbers)
    const = mmm.calculate_const(numbers, slope)
    variance = mmm.variance_with_regression(numbers, slope, const)
    std_dev = mmm.std_derivation(variance)
    student_val = 1.860
    assert mmm.calculate_interval(xk, numbers, std_dev, student_val) < 439.5455325


def test_CT21():
    mmm.input = lambda: '2'
    assert mmm.get_student() == 1.860


def teardown_method(self):
    mmm.input = input
