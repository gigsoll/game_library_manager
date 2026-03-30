FROM python:3.14-bookworm AS builder

# Work directory creation
RUN mkdir /app
WORKDIR /app

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install UV
COPY --from=ghcr.io/astral-sh/uv:0.10.12 /uv /uvx /bin/

# Disable UV development dependencies
ENV UV_NO_DEV=1

# Copy UV files
COPY pyproject.toml .
COPY uv.lock .

# Install dependencies
RUN uv sync --locked

# Create final container
FROM python:3.14-bookworm

# Create app user
RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app

# Copy the Python dependencies from the builder stage
COPY --from=builder /app/.venv/lib/python3.14/site-packages/ /usr/local/lib/python3.14/site-packages/

# Copy app files
WORKDIR /app
COPY --chown=appuser:appuser . .

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Switch to user
USER appuser

# Expose port 
EXPOSE 8000

# Prepare and set entrypoint
RUN chmod +x /app/entrypoint.prod.sh
ENTRYPOINT ["/app/entrypoint.prod.sh"]
