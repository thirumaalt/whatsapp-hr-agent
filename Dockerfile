# Playwright's official image already has Chromium + all system deps installed —
# building this yourself on python:3.12-slim means manually installing ~15 apt
# packages for headless Chrome. Not worth it.
FROM mcr.microsoft.com/playwright/python:v1.47.0-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Playwright browsers are already in this base image, but this is harmless
# and self-healing if the base image version drifts from your pinned playwright version.
RUN playwright install --with-deps chromium

COPY . .

# Persisted outside the image via volumes in docker-compose.yml:
# browser_data/ (WhatsApp session), resume/, output/, .env

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
