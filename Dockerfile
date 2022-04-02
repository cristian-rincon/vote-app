FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./backend/poetry.lock ./backend/pyproject.toml ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

# docker-compose-wait tool
ENV WAIT_VERSION 2.9.0
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait
COPY . .
