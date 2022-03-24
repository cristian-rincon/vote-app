FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install
COPY . .
