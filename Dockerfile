# 1) Base image: Python on Alpine Linux
FROM python:3.12-alpine

# 2) Install UV
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# 3) Sync dependencies and install project
RUN uv sync --all-groups

# 4) Run pytest
RUN . .venv/bin/activate && pytest

# 5) Launch the project
CMD [".venv/bin/python", "-m", "calculator"]
