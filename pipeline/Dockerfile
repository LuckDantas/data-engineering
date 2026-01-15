FROM python:3.13.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
# Copy dependency files first (better layer caching)
COPY pyproject.toml .python-version uv.lock ./

RUN uv sync --locked

# Set working directory
WORKDIR /app

#Add virtual environment to PATH so we can use installed packages
ENV PATH="/app/.venv/bin:$PATH"

# Copy application code
COPY ingest_data.py /app/ingest_data.py

# Set entrypoint
ENTRYPOINT ["uv","run","python", "ingest_data.py"]