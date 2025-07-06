import pytest
import source.my_func as my_func

def test_add():
    result = my_func.add(2, 3)
    assert result == 5, f"Expected 5, but got {result}"

def test_divide():
    result = my_func.divide(10, 2)
    assert result == 5, f"Expected 5, but got {result}"