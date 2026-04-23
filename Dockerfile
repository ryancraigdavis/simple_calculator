# 1) Base image — Python 3.12 on Alpine Linux
FROM python:3.12-alpine

# 2) Install UV
RUN pip install uv

# 3) Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Create virtual env, sync and install project
RUN uv venv .venv && \
    . .venv/bin/activate && \
    uv sync --include-all && \
    uv pip install -e .

# 4) Run pytest
RUN . .venv/bin/activate && pytest

# 5) Launch the calculator
CMD [".venv/bin/python", "src/calculator/calculator.py"]