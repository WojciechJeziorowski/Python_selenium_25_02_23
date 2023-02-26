import pytest_code
from pytest_code import *
def test_multiply():
    assert mulitply(4, 5) == 20
    assert mulitply(100, 1.1) == 110
    assert mulitply('mama', 5) == 0