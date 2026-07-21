from playwright.sync_api import Page


def open_community(page: Page, community_name: str):

    print(f"Searching : {community_name}")

    search = page.get_by_role(
        "textbox",
        name="Search or start a new chat"
    )

    # Wait until the search box is visible
    search.wait_for(state="visible", timeout=30000)

    # Clear existing text
    search.fill("")

    # Type the community name
    search.type(community_name, delay=100)

    page.wait_for_timeout(2000)

    # Click the first search result
    result = page.get_by_test_id("cell-frame-container").first
    result.wait_for(state="visible", timeout=10000)
    result.click()

    page.wait_for_timeout(1500)

    print("Community opened successfully")
