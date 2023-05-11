from pulp import value
from linear_optimization.examples import example1

def test_example1():
    x, y, problem = example1()
    assert value(x) == 2
    assert value(y) == 6
    assert value(problem.objective) == 36000
