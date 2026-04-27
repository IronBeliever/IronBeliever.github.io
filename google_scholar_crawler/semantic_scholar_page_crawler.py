import json
import os
import re
from datetime import datetime

from playwright.sync_api import sync_playwright

AUTHOR_URL = os.environ["SEMANTIC_SCHOLAR_AUTHOR_URL"]

def fetch_displayed_citations() -> int:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )
        )
        page.goto(AUTHOR_URL, wait_until="domcontentloaded", timeout=120000)
        page.wait_for_timeout(5000)
        body_text = page.locator("body").inner_text()
        browser.close()

    patterns = [
        r"\bCitations\s+(\d+)\b",
        r"\b(\d+)\s+Citations\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, body_text, re.IGNORECASE)
        if match:
            return int(match.group(1))

    raise RuntimeError("Could not find displayed citation count on Semantic Scholar author page.")

citation_count = fetch_displayed_citations()

os.makedirs("results", exist_ok=True)

with open("results/ss_data.json", "w", encoding="utf-8") as f:
    json.dump(
        {
            "updated": str(datetime.now()),
            "url": AUTHOR_URL,
            "citedby": citation_count,
        },
        f,
        ensure_ascii=False,
    )

with open("results/ss_data_shieldsio.json", "w", encoding="utf-8") as f:
    json.dump(
        {
            "schemaVersion": 1,
            "label": "Semantic Scholar",
            "message": str(citation_count),
        },
        f,
        ensure_ascii=False,
    )
