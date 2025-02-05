FROM python:3.12

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    VIRTUAL_ENV="/venv"

ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH"
RUN python -m venv $VIRTUAL_ENV

WORKDIR /app
ENV PYTHONPATH="/app:$PYTHONPATH"

RUN pip install poetry
COPY . .
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root
CMD python manage.py migrate\
    && python manage.py runserver 0.0.0.0:8000
