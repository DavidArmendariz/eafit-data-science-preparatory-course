from .solver import solve_problem
from pulp import LpProblem, LpMaximize, LpVariable


def example1():
    x = LpVariable("x", lowBound=0)
    y = LpVariable("y", lowBound=0)
    problem = LpProblem("Wyndsor_Glass_Company_Problem", LpMaximize)
    problem += 3000 * x + 5000 * y
    problem += x <= 4
    problem += 2 * y <= 12
    problem += 3 * x + 2 * y <= 18
    solve_problem(problem)
    return x, y, problem


if __name__ == "__main__":
    example1()
