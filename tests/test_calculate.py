import pytest
from calculate.operators import Operators

ops = Operators()

@pytest.mark.parametrize("operation,expected", [
    ("2 + 3", 5),
    ("0 + 5", 5)
])
def test_addition(operation, expected):
    result = ops.addition(operation)
    assert result == expected

@pytest.mark.parametrize("operation,expected", [
    ("5 - 3", 2),
    ("3 - 1", 2)
])
def test_substraction(operation, expected):
    result = ops.substraction(operation)
    assert result == expected

@pytest.mark.parametrize("operation,expected", [
    ("2 * 3", 6),
    ("3 * 4", 12)
])
def test_multiplication(operation, expected):
    result = ops.multiplication(operation)
    assert result == expected

@pytest.mark.parametrize("operation,expected", [
    ("6 / 3", 2),
    ("4 / 2", 2)
])
def test_division(operation, expected):
    result = ops.division(operation)
    assert result == expected
