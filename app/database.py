"""
app/database.py
SQLAlchemy engine + session setup for the multi-user version.
Replaces reading everything from config.py at import time.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Local dev: sqlite. Production: postgres via env var.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./hr_agent.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """FastAPI dependency — yields a session, always closes it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
