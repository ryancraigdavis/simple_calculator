# Simple Calculator

This program takes a few different inputs and can spit out various results from mathematical formulas.
Your task is to create simple unit tests for each of these formulas.

## Step 1: uv
To set up the project with uv you want to do the following things.
### a) `uv init` which will create the uv project
### b) The project uses a `src` layout with the following structure:
```
    simple_calculator
    ├── src
    │   └── calculator
    │       ├── __init__.py
    │       └── ...
    ├── .gitignore
    ├── pyproject.toml
    ├── uv.lock
    └── ...
```
uv automatically discovers packages under `src/` when using the `uv_build` build backend, so no extra include configuration is needed.
### c) Add your dependencies
Run `uv add <package>` to install dependencies. For dev-only dependencies, use `uv add --group dev <package>`.
### d) Sync and run
Run `uv sync` to create the virtual environment and install all dependencies (including your own project as an editable package). Then use `uv run <command>` to run commands within the environment.
