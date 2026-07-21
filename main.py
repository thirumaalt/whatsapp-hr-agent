"""
main.py
Single entrypoint. All actual routes live in app/api.py — this file just
re-exports that app so `uvicorn main:app` (and your Dockerfile CMD, which
already points at main:app) keeps working unchanged.

Previously there were THREE separate FastAPI() instances in this project
(root main.py, app/main.py, app/api.py) with routes split across them —
only app.api's routes (scan/jobs/emails, now +register/login/me) were
reachable when running `uvicorn main:app`, since this file's own bare
FastAPI() had no routes registered. Consolidated into one app.
"""
from app.api import app

__all__ = ["app"]
