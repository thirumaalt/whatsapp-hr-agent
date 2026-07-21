from fastapi import FastAPI
from app.scanner import scan_whatsapp
from app import cache

app = FastAPI()


@app.get("/")
def home():

    return {
        "status": "running",
        "message": "WhatsApp Job API"
    }


@app.get("/scan")
def scan():

    jobs = scan_whatsapp()

    return {
        "status": "success",
        "jobs_found": len(jobs)
    }


@app.get("/emails")
def get_emails():

    return {
        "count": len(cache.emails),
        "emails": cache.emails
    }


@app.get("/jobs")
def get_jobs():

    return {
        "count": len(cache.jobs),
        "jobs": cache.jobs
    }
