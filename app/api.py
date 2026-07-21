from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from app.scanner import scan_whatsapp
from app import cache
from app.database import engine, get_db, Base
from app.models import User
from app.auth import hash_password, verify_password, create_access_token, get_current_user

app = FastAPI()

# Creates users/smtp_settings/whatsapp_settings/resumes/jobs tables if they
# don't exist yet. Safe to run on every startup.
Base.metadata.create_all(bind=engine)


class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@app.get("/")
def home():

    return {
        "status": "running",
        "message": "WhatsApp Job API"
    }


@app.post("/register", response_model=TokenResponse)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        name=payload.name,
        email=payload.email,
        hashed_password=hash_password(payload.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token(user.id)
    return TokenResponse(access_token=token)


@app.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # OAuth2 form spec calls the email field "username"
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    token = create_access_token(user.id)
    return TokenResponse(access_token=token)


@app.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return {"id": current_user.id, "name": current_user.name, "email": current_user.email}


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
