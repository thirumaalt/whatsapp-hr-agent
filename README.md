<div align="center">

# 🚀 WhatsApp HR Agent

### Intelligent WhatsApp Job Automation using Playwright, FastAPI & Gmail SMTP

Automatically scans WhatsApp placement communities, extracts HR job postings, stores them in Excel, detects duplicates, and sends your resume to HR email IDs — fully automated.

---

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green?style=for-the-badge&logo=playwright)
![FastAPI](https://img.shields.io/badge/FastAPI-Web_API-009688?style=for-the-badge&logo=fastapi)
![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-E95420?style=for-the-badge&logo=ubuntu)
![Linux](https://img.shields.io/badge/Linux-Compatible-FCC624?style=for-the-badge&logo=linux)
![SMTP](https://img.shields.io/badge/Gmail-SMTP-red?style=for-the-badge&logo=gmail)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

---

### ⭐ Features

📱 WhatsApp Community Scanner

📧 Automatic Resume Email Sender

📊 Excel Database

🔍 Duplicate Detection

📌 Checkpoint-Based Incremental Scan

🤖 Browser Automation using Playwright

⏰ Cron Scheduler

📄 HTML Email Template

📈 Production Ready Workflow

</div>

---

# 📖 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [Technology Stack](#-technology-stack)
- [Folder Structure](#-folder-structure)
- [Project Workflow](#-project-workflow)
- [Screenshots](#-screenshots)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Running the Project](#-running-the-project)
- [Cron Scheduler](#-cron-scheduler)
- [API Endpoints](#-api-endpoints)
- [Future Roadmap](#-future-roadmap)
- [Author](#-author)

---

# 📌 Project Overview

Recruiters frequently post job openings inside WhatsApp placement communities.

Checking hundreds of messages manually every day is time-consuming and often results in missed opportunities.

This project automates the entire process.

Instead of manually reading every WhatsApp message, the application automatically:

- Opens WhatsApp Web
- Reads new placement messages
- Expands **Read More**
- Merges split messages
- Extracts HR details
- Saves everything into Excel
- Detects duplicate jobs
- Sends your resume automatically
- Updates checkpoint for future scans

The automation runs twice daily using Cron Scheduler without manual intervention.

---

# ✨ Key Features

## 📱 WhatsApp Automation

- Automated browser using Playwright
- Persistent login session
- Reads latest placement posts
- Opens WhatsApp Community automatically

---

## 📄 Smart Message Processing

- Expand **Read More**
- Merge continuation messages
- Ignore unrelated conversations
- Handle multiline job descriptions

---

## 📧 Resume Automation

- Detect HR email IDs
- Generate HTML email
- Attach resume automatically
- Gmail SMTP integration

---

## 📊 Excel Database

Stores

- Company
- Job Title
- Email
- Location
- Experience
- Apply Link
- Mail Status
- Date

---

## 🔁 Duplicate Detection

Previously processed jobs are automatically skipped.

No duplicate entries.

No duplicate emails.

---

## 📌 Checkpoint System

Stores last processed message.

Future scans read only newly posted jobs.

Very fast execution.

---

# 🏗 Project Architecture

```text
                         WhatsApp Community
                                 │
                                 ▼
                    Playwright Browser Automation
                                 │
                                 ▼
                      Read Latest Messages
                                 │
                                 ▼
                     Expand "Read More" Text
                                 │
                                 ▼
                     Merge Multi-line Messages
                                 │
                                 ▼
                      Parse Job Information
                                 │
                ┌────────────────┴────────────────┐
                ▼                                 ▼
          Excel Database                  Gmail Mailer
                │                                 │
                └────────────────┬────────────────┘
                                 ▼
                      Update Checkpoint File
                                 │
                                 ▼
                     Cron Scheduler (10 AM / 4 PM)
```

---

# ⚙ Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.12 |
| Automation | Playwright |
| API | FastAPI |
| Email | Gmail SMTP |
| Spreadsheet | OpenPyXL |
| Scheduler | Cron |
| OS | Ubuntu Linux |
| Browser | Google Chrome |
| Version Control | Git & GitHub |

---

> ---

# 📂 Folder Structure

```text
whatsapp-hr-agent/
│
├── app/
│   ├── api.py                 # FastAPI Endpoints
│   ├── scanner.py             # Main Scanner Logic
│   ├── reader.py              # Reads WhatsApp Messages
│   ├── parser.py              # Extract Job Information
│   ├── excel.py               # Excel Operations
│   ├── mailer.py              # Gmail SMTP Mail Sender
│   ├── checkpoint.py          # Checkpoint Management
│   ├── config.py              # Application Configuration
│   ├── whatsapp.py            # WhatsApp Utilities
│   └── search.py              # Search Functions
│
├── output/
│   └── jobs.xlsx              # Extracted Job Database
│
├── resume/
│   └── dhanraj_solu.pdf       # Resume Attachment
│
├── templates/
│   └── mail.html              # HTML Email Template
│
├── browser_data/              # Playwright Browser Profile
│
├── logs/
│   └── cron.log               # Cron Execution Logs
│
├── checkpoint.json            # Last Processed Message
├── requirements.txt
├── run.py
├── README.md
└── .gitignore
```

---

# 🔄 End-to-End Workflow

```text
                       WhatsApp Community
                                │
                                ▼
                     Open WhatsApp Web
                                │
                                ▼
                 Search Placement Community
                                │
                                ▼
                 Read Latest Available Messages
                                │
                                ▼
                 Expand "Read More" Automatically
                                │
                                ▼
                Merge Split / Continued Messages
                                │
                                ▼
                 Extract Job Related Information
                                │
         ┌──────────────┬───────────────┬──────────────┐
         ▼              ▼               ▼              ▼
      Company         Email         Experience      Location
         │
         ▼
      Duplicate Check
         │
         ▼
      Save into Excel
         │
         ▼
     Attach Resume PDF
         │
         ▼
     Send Gmail to HR
         │
         ▼
     Update Checkpoint
         │
         ▼
   Wait for Next Cron Schedule
```

---

# 🖼 Screenshots

## WhatsApp Community Scanner

> Place your scanner screenshot here.

```text
images/whatsapp_scan.png
```

```markdown
![WhatsApp Scanner](images/whatsapp_scan.png)
```

---

## Excel Output

Shows all extracted job information.

```text
images/jobs_excel.png
```

```markdown
![Excel Output](images/jobs_excel.png)
```

---

## Resume Email

Screenshot of automatically generated email.

```text
images/email_sent.png
```

```markdown
![Resume Mail](images/email_sent.png)
```

---

## Terminal Output

Scanner execution.

```text
images/terminal_output.png
```

```markdown
![Terminal](images/terminal_output.png)
```

---

## Cron Execution Log

Automatic scheduler execution.

```text
images/cron_logs.png
```

```markdown
![Cron Logs](images/cron_logs.png)
```

---

# 🚀 Installation

Clone Repository

```bash
git clone https://github.com/dhanrajp3005-hesha/whatsapp-hr-agent.git
```

Go to Project

```bash
cd whatsapp-hr-agent
```

Create Virtual Environment

```bash
python3 -m venv venv
```

Activate Environment

Ubuntu

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Verify Installation

```bash
python --version
pip --version
```

---

# ⚙ Configuration

Open

```text
app/config.py
```

Configure

- Gmail Email
- Gmail App Password
- Resume Path
- WhatsApp Community Name

Example

```python
EMAIL = "yourmail@gmail.com"

APP_PASSWORD = "your_app_password"

COMMUNITY_NAME = "Zenbyte Current Placement"

RESUME_PATH = "resume/dhanraj_solu.pdf"
```

---

# 📧 Gmail App Password Setup

Enable

- Google 2-Step Verification

Create

Google Account

↓

Security

↓

App Passwords

↓

Mail

↓

Other Device

↓

Generate Password

Copy generated password into

```text
config.py
```

Never use your normal Gmail password.

---

# 📱 WhatsApp Setup

Run

```bash
python run.py
```

First time

- WhatsApp Web opens
- Scan QR Code
- Browser session saved

Next executions

✅ No QR Scan Required

Persistent login is maintained inside

```text
browser_data/
```

---

# 🧪 First Run

Execute

```bash
python run.py
```

Expected Output

```text
WhatsApp HR Agent Started

↓

Opening WhatsApp

↓

Reading Messages

↓

Extracting Jobs

↓

Saving Excel

↓

Sending Resume

↓

Updating Checkpoint

↓

Completed Successfully
```

---

> ---

# ⏰ Cron Scheduler

The project supports fully automated execution using Linux Cron Scheduler.

Instead of manually running the application every day, Cron automatically starts the scanner at scheduled times.

Current Schedule

| Time | Action |
|------|--------|
| 10:00 AM | Scan WhatsApp & Send Resume |
| 04:00 PM | Scan WhatsApp & Send Resume |

---

## Edit Cron

Open Cron

```bash
crontab -e
```

Example

```bash
DISPLAY=:1
XAUTHORITY=/run/user/1001/gdm/Xauthority

0 10 * * * cd ~/projects/whatsapp-hr-agent && /home/<username>/projects/whatsapp-hr-agent/venv/bin/python run.py >> logs/cron.log 2>&1

0 16 * * * cd ~/projects/whatsapp-hr-agent && /home/<username>/projects/whatsapp-hr-agent/venv/bin/python run.py >> logs/cron.log 2>&1
```

---

## Verify Cron

```bash
crontab -l
```

---

## Check Cron Logs

```bash
cat logs/cron.log
```

or

```bash
tail -f logs/cron.log
```

---

# 🌐 FastAPI API

The project also provides REST APIs for triggering scans and monitoring application status.

Start API Server

```bash
uvicorn app.api:app --reload
```

Default URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Available Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Application Status |
| POST | /scan | Start Scanner |
| GET | /jobs | Get Extracted Jobs |

---

# 📄 Logging

Every execution is recorded.

Example

```text
Application Started

Opening Browser

Reading Messages

Parsing Jobs

Saving Excel

Sending Email

Checkpoint Updated

Application Finished
```

---

# 📊 Excel Output

Each extracted job is stored in Excel.

Columns

| Column | Description |
|---------|-------------|
| Company | Company Name |
| Job Title | Position |
| Email | HR Email |
| Experience | Required Experience |
| Location | Job Location |
| Apply Link | Application URL |
| Mail Sent | Yes / No |
| Date | Processing Date |

---

# 📌 Checkpoint System

The application remembers the last processed message.

Example

```json
{
    "last_header": "Python Developer",
    "last_email": "hr@company.com"
}
```

Benefits

- Faster execution

- No duplicate scanning

- No duplicate email

- Incremental processing

---

# 🔒 Security

Sensitive information should never be committed to GitHub.

Recommended

```
config.py
```

Future Improvement

```
.env
```

Sensitive Data

- Gmail Password

- App Password

- Email Address

- Resume Path

---

# ⚡ Performance

Average Scan

| Operation | Time |
|-----------|------|
| Open Browser | 5 sec |
| Read Messages | 10 sec |
| Parse Jobs | 2 sec |
| Save Excel | 1 sec |
| Send Emails | Depends on Job Count |
| Total | ~20-30 sec |

---

# ❗ Troubleshooting

## Browser Doesn't Open

Check

```bash
echo $DISPLAY
```

Should return

```
:1
```

---

## QR Code Appears Every Time

Delete old browser profile

```bash
rm -rf browser_data/
```

Login once again.

---

## Gmail Authentication Failed

Verify

- Gmail 2-Step Verification Enabled

- App Password Used

- Normal Password NOT Used

---

## Excel Not Updating

Check

```bash
output/jobs.xlsx
```

Ensure the file is not already open in Microsoft Excel or LibreOffice.

---

## No New Jobs Found

Possible Reasons

- No new WhatsApp messages

- Duplicate job detected

- Checkpoint already updated

---

# 💡 Frequently Asked Questions

### Does it send duplicate emails?

No.

Duplicate detection prevents repeated emails.

---

### Does it read old WhatsApp messages?

Currently it processes only new messages.

History Import support is planned.

---

### Can it work without Cron?

Yes.

Simply run

```bash
python run.py
```

---

### Can it run on Windows?

Possible.

Ubuntu/Linux is recommended for Cron automation.

---

### Can I change the WhatsApp community?

Yes.

Update the Community Name inside

```
app/config.py
```

---

### Can I customize the email template?

Yes.

Edit

```
templates/mail.html
```

---

> ---

# 🛣️ Future Roadmap

The following features are planned for future releases.

| Status | Feature |
|---------|----------|
| ✅ | WhatsApp Community Scanner |
| ✅ | Resume Email Automation |
| ✅ | Excel Database |
| ✅ | Duplicate Detection |
| ✅ | Gmail SMTP Integration |
| ✅ | Checkpoint Based Incremental Scan |
| ✅ | Cron Scheduler |
| ⏳ | Full History Import |
| ⏳ | AI Job Filtering |
| ⏳ | Telegram Notifications |
| ⏳ | Multiple Community Support |
| ⏳ | PostgreSQL Database |
| ⏳ | Docker Support |
| ⏳ | Dashboard UI |
| ⏳ | Resume Recommendation Engine |
| ⏳ | Multi-user Login |

---

# 🧩 Upcoming Enhancements

### 🤖 AI Based Job Filtering

Automatically filter jobs based on

- Python
- DevOps
- AWS
- Kubernetes
- Docker
- Linux

Only matching jobs will be stored and emailed.

---

### 📱 Telegram Notification

Receive instant notification whenever a new job is found.

Example

```
New Job Found

Company : ABC Technologies

Role : DevOps Engineer

Experience : 3 Years

Email :
hr@company.com
```

---

### 🐳 Docker Support

One command deployment

```bash
docker compose up -d
```

---

### 📊 Dashboard

Future web dashboard

Features

- Total Jobs
- Today's Jobs
- Total Emails Sent
- Failed Emails
- Search Jobs
- Download Excel
- Resume Upload
- Manual Scan

---

### 🗄 PostgreSQL Support

Current

Excel Database

Future

PostgreSQL

Benefits

- Faster Search

- Better Reporting

- Multiple Users

- API Integration

---

# 🤝 Contributing

Contributions are always welcome.

Steps

1. Fork Repository

2. Create New Branch

```bash
git checkout -b feature/new-feature
```

3. Commit Changes

```bash
git commit -m "Added New Feature"
```

4. Push

```bash
git push origin feature/new-feature
```

5. Create Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify and improve the project.

---

# 📌 Project Statistics

| Metric | Details |
|---------|----------|
| Language | Python |
| Framework | FastAPI |
| Browser Automation | Playwright |
| Email Service | Gmail SMTP |
| Database | Excel (OpenPyXL) |
| Scheduler | Cron |
| Operating System | Ubuntu Linux |
| Version Control | Git & GitHub |

---

# 🎯 Interview Talking Points

This project demonstrates practical experience in

- Browser Automation

- Web Scraping

- Process Automation

- Python Development

- API Development

- File Processing

- Email Automation

- Linux Administration

- Scheduling with Cron

- Production Logging

- Error Handling

- Software Architecture

- Git Version Control

- Real-world Automation

---

# 📸 Demo Workflow

```
WhatsApp Community

        │

        ▼

Read New Messages

        │

        ▼

Extract HR Details

        │

        ▼

Save Excel

        │

        ▼

Detect Duplicates

        │

        ▼

Send Resume

        │

        ▼

Update Checkpoint

        │

        ▼

Wait for Next Cron Execution
```

---

# 📈 Version History

## Version 1.0.0

Initial Release

Features

- WhatsApp Scanner

- Resume Mail Automation

- Excel Storage

- Duplicate Detection

- Checkpoint System

- Cron Scheduler

---

## Planned Version 2.0

- AI Filtering

- Dashboard

- Docker

- PostgreSQL

- Telegram Bot

- History Import

---

# 👨‍💻 Author

**Dhanraj P**

Cloud & DevOps Engineer

📍 Chennai, India

### Technical Skills

- AWS

- DevOps

- Python

- Linux

- Docker

- Kubernetes

- Terraform

- Jenkins

- GitHub Actions

- Playwright

- FastAPI

---

# ⭐ Support

If you found this project useful,

please consider giving it a ⭐ on GitHub.

It helps other developers discover the project.

---

# 🙏 Acknowledgements

Special thanks to the open-source community.

This project uses

- Python

- Playwright

- FastAPI

- OpenPyXL

- Gmail SMTP

- Ubuntu Linux

Without these amazing tools, this project wouldn't have been possible.

---

<div align="center">

# ⭐ Thank You ⭐

### If you like this project,

### don't forget to Star ⭐ the repository.

---

Made with ❤️ using Python, Playwright & FastAPI

</div>
