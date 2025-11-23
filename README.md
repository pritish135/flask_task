# Minimal Flask App

This is a minimal Flask application for testing and development.

Quick start

1. Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

- Option A (recommended for quick test):

```bash
python app.py
```

- Option B (using `flask run`):

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

Endpoints

- `GET /` — simple HTML index with links
- `GET /hello/<name>` — returns JSON greeting
- `GET /health` — returns `{ "status": "ok" }`

Examples

```bash
curl http://127.0.0.1:5000/hello/Alice
# {"message":"Hello, Alice!"}
```

Docker
------

Build and run with `docker compose` (newer Docker CLI):

```bash
docker compose up --build
```

Or with legacy `docker-compose`:

```bash
docker-compose up --build
```

This builds the image from the repository root (the `build` context is `.`) and maps container port `5000` to the host.

You can also build and run the image manually:

```bash
docker build -t minimal-flask-app .
docker run --rm -p 5000:5000 minimal-flask-app
```

Notes on production run
----------------------

- The container uses `gunicorn` as the production WSGI server. The default number of workers is controlled by the `WEB_CONCURRENCY` environment variable (default: `2`).
- You can set `WEB_CONCURRENCY` via `docker compose` or `docker run`. Example:

```bash
docker compose run -e WEB_CONCURRENCY=4 web
# or
docker run --rm -p 5000:5000 -e WEB_CONCURRENCY=4 minimal-flask-app
```

The container listens on the port defined by the `PORT` environment variable (default `5000`).

