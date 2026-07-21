"""
app/models.py
Core tables. One row per user in each settings table = per-user isolation.
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)  # never store plaintext
    created_at = Column(DateTime, default=datetime.utcnow)

    smtp_settings = relationship("SMTPSettings", back_populates="user", uselist=False)
    whatsapp_settings = relationship("WhatsAppSettings", back_populates="user", uselist=False)
    resume = relationship("Resume", back_populates="user", uselist=False)
    jobs = relationship("Job", back_populates="user")


class SMTPSettings(Base):
    __tablename__ = "smtp_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    smtp_email = Column(String, nullable=False)
    encrypted_app_password = Column(Text, nullable=False)  # Fernet-encrypted, see security.py
    host = Column(String, default="smtp.gmail.com")
    port = Column(Integer, default=587)

    user = relationship("User", back_populates="smtp_settings")


class WhatsAppSettings(Base):
    __tablename__ = "whatsapp_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    community_name = Column(String, nullable=False)
    # path to this user's isolated Playwright browser profile dir, e.g. browser_data/user_3/
    browser_profile_path = Column(String, nullable=False)
    session_logged_in = Column(Boolean, default=False)

    user = relationship("User", back_populates="whatsapp_settings")


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    resume_path = Column(String, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="resume")


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    company = Column(String)
    role = Column(String)
    email = Column(String)
    experience = Column(String)
    location = Column(String)
    apply_link = Column(String)
    mail_sent = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="jobs")
