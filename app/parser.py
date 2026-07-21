import re

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
URL_REGEX = r"https?://[^\s]+"

LOCATION_REGEX = r"Location\s*[:\-]\s*(.+)"
EXPERIENCE_REGEX = r"Experience\s*[:\-]\s*(.+)"


def extract_emails(messages):

    emails = []

    for item in messages:

        message = item["message"]

        found = re.findall(EMAIL_REGEX, message)

        emails.extend(found)

    # Remove duplicates while preserving order
    emails = list(dict.fromkeys(emails))

    return emails


def extract_job_details(messages):

    jobs = []

    for item in messages:

        header = item["header"]
        message = item["message"]

        emails = re.findall(EMAIL_REGEX, message)
        links = re.findall(URL_REGEX, message)

        email = emails[0] if emails else None
        apply_link = links[0] if links else None

        location = None
        experience = None

        location_match = re.search(
            LOCATION_REGEX,
            message,
            re.IGNORECASE
        )

        if location_match:
            location = location_match.group(1).strip()

        experience_match = re.search(
            EXPERIENCE_REGEX,
            message,
            re.IGNORECASE
        )

        if experience_match:
            experience = experience_match.group(1).strip()

        if email:

            jobs.append(
                {
                    "header": header,
                    "company": "",
                    "job_title": "",
                    "email": email,
                    "location": location,
                    "experience": experience,
                    "apply_link": apply_link,
                    "message": message
                }
            )

    return jobs
