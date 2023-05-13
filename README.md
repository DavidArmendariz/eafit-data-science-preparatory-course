# Data Science preparatory course

## Prerrequisites

* Pyenv
* Pipenv

Once you installed pipenv, create the virtual environment:

```terminal
pipenv install
```

## Setup in VSCode

* Choose the correct Python interpreter, which should be the one created by Pipenv.

## Tests

* Run `pipenv shell` and then `pytest`.
* If you want to show the output of print statements, run it like this: `pytest -s`

## How to run files

* This project is comprised of packages. To run an individual module within a package, you have to do it like this:

```terminal
python -m package.module
```

Example:

```terminal
python -m linear_optimization.examples
```
