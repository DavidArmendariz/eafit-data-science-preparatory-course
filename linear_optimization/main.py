from pulp import LpProblem, LpStatus, value

def solve_problem(problem: LpProblem):
    solution = problem.solve()
    print(f"Solution status: {LpStatus[solution]}")
    print(f"Optimal cost: {value(problem.objective)}")
    for variable in problem.variables():
        print(f"Optimal value of {variable}: {value(variable)}")
    return solution
