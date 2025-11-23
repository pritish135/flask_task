FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

WORKDIR /app

# Install runtime dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy application code
COPY . /app

# Create a limited user to run the app
RUN groupadd -r app && useradd -r -g app app \
    && chown -R app:app /app

USER app

EXPOSE ${PORT}

# Production-ready command using gunicorn. Respects WEB_CONCURRENCY and PORT env vars.
# Use the shell form to allow environment variable expansion.
CMD ["sh", "-c", "exec gunicorn -w ${WEB_CONCURRENCY:-2} -b 0.0.0.0:${PORT} --access-logfile - --error-logfile - app:app"]
