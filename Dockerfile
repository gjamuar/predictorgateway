FROM python:3.12

WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy project dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root --no-dev

# Copy the rest of the project files
COPY . .

CMD ["sh", "-c", "poetry run gunicorn run:app -w 4 --bind 0.0.0.0:${PORT:-9900}"]