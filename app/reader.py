from playwright.sync_api import Page
import re


def expand_read_more(page: Page):

    print("=" * 80)
    print("Expanding 'Read more' sections...")
    print("=" * 80)

    expanded = 0

    while True:

        read_more = page.get_by_text("Read more")

        if read_more.count() == 0:
            break

        try:
            read_more.first.scroll_into_view_if_needed()
            read_more.first.click(timeout=3000)
            page.wait_for_timeout(500)
            expanded += 1

        except Exception:
            break

    print(f"Expanded Read More : {expanded}")
    print("=" * 80)


def is_new_message(header: str):

    if not header:
        return False

    header = header.strip()

    # WhatsApp sender header
    if header.startswith("["):
        return True

    return False


def read_messages(page: Page):

    print("=" * 80)
    print("Reading latest messages...")
    print("=" * 80)

    page.wait_for_timeout(2000)

    expand_read_more(page)

    page.wait_for_timeout(1000)

    print("Current Page Title :", page.title())
    print("Current URL        :", page.url)

    messages = page.locator("[data-pre-plain-text]")

    total = messages.count()

    print(f"Total DOM Messages : {total}")

    raw_messages = []

    for i in range(total):

        try:

            container = messages.nth(i)

            header = container.get_attribute("data-pre-plain-text") or ""

            text = container.inner_text().strip()

            raw_messages.append(
                {
                    "header": header.strip(),
                    "message": text
                }
            )

        except Exception as e:

            print(f"Error reading message {i+1}: {e}")

    print("=" * 80)
    print("Merging continuation messages...")
    print("=" * 80)

    merged = []

    current = None

    for item in raw_messages:

        header = item["header"]
        message = item["message"]

        if is_new_message(header):

            if current:
                merged.append(current)

            current = {
                "header": header,
                "message": message
            }

        else:

            if current:

                current["message"] += "\n\n" + message

            else:

                current = {
                    "header": header,
                    "message": message
                }

    if current:
        merged.append(current)

    print(f"Actual Job Posts : {len(merged)}")

    print("=" * 80)

    for i, item in enumerate(merged, start=1):

        print("=" * 80)
        print(f"Job Post {i}")
        print("=" * 80)

        print("Header")
        print("-" * 80)
        print(item["header"])

        print("\nMessage")
        print("-" * 80)
        print(item["message"][:600])

        if len(item["message"]) > 600:
            print("\n...truncated...\n")

    print("=" * 80)
    print("Finished Reading Messages")
    print("=" * 80)

    return merged
