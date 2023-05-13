from .integration_methods import riemann_int, monte_carlo_int


def example1():
    def f(x):
        return x**2

    return riemann_int(f, lower_bound=0, upper_bound=2, partitions=20)


def example2():
    def f(x):
        return x**2

    return monte_carlo_int(f, lower_bound=0, upper_bound=2, n=1000)


if __name__ == "__main__":
    print(f"Integral of x^2 from 0 to 2 using Riemann: {example1()}")
    print(f"Integral of x^2 from 0 to 2 using Monte Carlo: {example2()}")
