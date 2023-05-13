import numpy as np


def riemann_int(f, lower_bound, upper_bound, partitions):
    if not callable(f):
        raise ValueError("f must be a function of one variable")
    a = lower_bound
    b = upper_bound
    n = partitions
    h = (b - a) / n
    j = np.arange(1, n)
    xj = a + j * h
    approx = np.sum(f(xj) * h)
    return approx


def monte_carlo_int(f, lower_bound, upper_bound, n):
    if not callable(f):
        raise ValueError("f must be a function of one variable")
    a = lower_bound
    b = upper_bound
    x = np.linspace(a, b, 1000)
    fx = f(x)
    d = np.max(fx)
    x_random = np.random.uniform(a, b, n)
    y_random = np.random.uniform(0, d, n)
    rectangle_area = d * (b - a)
    p = np.sum(y_random < f(x_random))
    return rectangle_area * (p / n)


def midpoint_int(f, lower_bound, upper_bound, n):
    if not callable(f):
        raise ValueError("f must be a function of one variable")
    a = lower_bound
    b = upper_bound
    h = (b - a) / n
    j = list(range(1, n))
    xj = [a + j[i] * h for i in range(len(j))]
    approx = sum([f(x + (h / 2)) * h for x in xj])
    return approx


def trapezoid_int(f, lower_bound, upper_bound, n):
    if not callable(f):
        raise ValueError("f must be a function of one variable")
    a = lower_bound
    b = upper_bound
    h = (b - a) / n
    j = list(range(1, n))
    xj = [a + j[i] * h for i in range(len(j))]
    approx = (h / 2) * (f(a) + 2 * sum([f(x) for x in xj]) + f(b))
    return approx
