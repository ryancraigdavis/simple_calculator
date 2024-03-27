# Simple Calculator

This program takes a few different inputs and can spit out various results from mathematical formulas.
Your task is to create simple unit tests for each of these formulas.

## Step 1: Poetry
To set up Poetry you want to do the following things.</br>
### a) `poetry init` which will create the poetry project
### b) You want to then add an include section to your project with the destination of your start script. 
In this case mine is called `__init__.py` and sits in the following structure:
```
    quart_example
    ├── src
    │   └── poetry_example
    │       ├── __init__.py
    │       └── ...
    ├── .gitignore
    ├── pyproject.toml
    ├── poetry.lock
    └── ...
```
Thus my include statement looks like this (it goes in the `[tool.poetry]` section at the top level):
```
packages = [
  { include = "src", from = "." }
]
```
What does this do? It allows you to install your own project as a package into your venv. This allows you to create scripts you can run which is critical for deployment.
### c) Add your dependencies
In this case you can run `poetry add quart` to install quart and then whatever else you need
### d) Activate your poetry shell and install
Run `poetry shell` in order to launch your virtual environment and then run `poetry install` to install all dependencies including your own package. You need a README.md or the installing of your own project will fail.
