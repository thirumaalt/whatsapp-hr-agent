from pathlib import Path
from dotenv import load_dotenv
import os

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================================
# WhatsApp Configuration
# ==========================================================

WHATSAPP_URL = "https://web.whatsapp.com"

BROWSER_DATA_DIR = BASE_DIR / "browser_data"

HEADLESS = False

WAIT_TIME = 30000

# ==========================================================
# Resume
# ==========================================================

RESUME_PATH = BASE_DIR / "resume" / "dhanraj_solu.pdf"

# ==========================================================
# Excel
# ==========================================================

EXCEL_FILE = BASE_DIR / "output" / "jobs.xlsx"

# ==========================================================
# HTML Template
# ==========================================================

MAIL_TEMPLATE = BASE_DIR / "templates" / "mail.html"

# ==========================================================
# Mail Subject
# ==========================================================

MAIL_SUBJECT = "Application for AWS DevOps Engineer | 5 Years Experience"

# ==========================================================
# Mail Delay (Seconds)
# ==========================================================

MAIL_DELAY = 15

# ==========================================================
# Logs
# ==========================================================

LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "mailer.log"

# Create logs folder if not exists
LOG_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Gmail SMTP Configuration
# ==========================================================

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

FROM_EMAIL = os.getenv("FROM_EMAIL")

# ==========================================================
# Validation
# ==========================================================

required = [
    SMTP_USERNAME,
    SMTP_PASSWORD,
    FROM_EMAIL,
]

if not all(required):
    raise ValueError(
        "SMTP configuration missing. Please check your .env file."
    )
