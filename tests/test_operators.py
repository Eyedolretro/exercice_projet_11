import pytest
from calculate.operators import Operators

ops = Operators()

@pytest.mark.parametrize("operation,expected", [
    ("2 + 3", 5),
    ("0 + 5", 5),
    ("2.5 + 3.5", 6.0)
])
def test_addition(operation, expected):
    result = ops.addition(operation)
    assert result == expected

@pytest.mark.parametrize("operation,expected", [
    ("5 - 3", 2),
    ("3 - 1", 2),
    ("5.5 - 2.2", 3.3)
])
def test_substraction(operation, expected):
    result = ops.substraction(operation)
    assert result == expected

@pytest.mark.parametrize("operation,expected", [
    ("2 * 3", 6),
    ("3 * 4", 12),
    ("2.5 * 4.0", 10.0)
])
def test_multiplication(operation, expected):
    result = ops.multiplication(operation)
    assert result == expected

@pytest.mark.parametrize("operation,expected", [
    ("6 / 3", 2),
    ("4 / 2", 2),
    ("5.0 / 2.0", 2.5)
])
def test_division(operation, expected):
    result = ops.division(operation)
    assert result == expected

def test_division_by_zero():
    result = ops.division("5 / 0")
    assert result is None
