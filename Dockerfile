FROM python:3.12-alpine

RUN apk add --no-cache curl gcc musl-dev

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . .

RUN uv sync --frozen

RUN uv run pytest

CMD ["uv", "run", "python", "main.py"]
