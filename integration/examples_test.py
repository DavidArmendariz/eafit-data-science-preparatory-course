from .examples import example1
from pytest import approx

def test_example1():
    result = example1()
    assert approx(result) == 2.47