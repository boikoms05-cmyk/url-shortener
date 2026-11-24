# URL Shortener Microservice (DevOps Portfolio Project)

A containerized URL shortening microservice built with FastAPI and Redis, complete with real-time observability (Prometheus + Grafana) and an automated CI pipeline via GitHub Actions.

## Tech Stack
* **Backend:** Python 3.11, FastAPI, Uvicorn, Pydantic
* **Database:** Redis 7 (persistent storage with Docker Volumes)
* **Containerization & Orchestration:** Docker, Docker Compose
* **Observability:** Prometheus, Grafana (`prometheus-fastapi-instrumentator`)
* **CI/CD:** GitHub Actions (`flake8` linting + automated Docker image build check)

## Architecture
1. **App (`:8000`)** — Accepts long URLs via `POST /shorten`, generates a unique 6-character short ID, stores the mapping in Redis, and handles HTTP `307` redirects via `GET /{short_id}`. Exposes application metrics at `/metrics`.
2. **Redis (`:6379`)** — In-memory key-value store persisting `short_id -> original_url` mappings.
3. **Prometheus (`:9090`)** — Scrapes application telemetry every 5 seconds (RPS, latency, HTTP status codes).
4. **Grafana (`:8080`)** — Visualizes real-time traffic and service health dashboards.

## Quick Start

1. Clone the repository:
   ```bash
   git clone [https://github.com/](https://github.com/)boikoms05-cmyk/url-shortener.git
   cd url-shortener