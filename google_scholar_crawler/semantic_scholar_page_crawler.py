import json
import os
import re
from datetime import datetime

from playwright.sync_api import sync_playwright

AUTHOR_URL = os.environ["SEMANTIC_SCHOLAR_AUTHOR_URL"]

def parse_citation_count_from_text(text: str) -> int | None:
    normalized = re.sub(r"\s+", " ", text)
    patterns = [
        r"\bCitations?\s+(\d[\d,]*)\b",
        r"\b(\d[\d,]*)\s+Citations?\b",
        r"\bCitations?\s*[:\-]?\s*(\d[\d,]*)\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, normalized, re.IGNORECASE)
        if match:
            return int(match.group(1).replace(",", ""))
    return None


def parse_citation_count_from_html(html: str) -> int | None:
    author_id = AUTHOR_URL.rstrip("/").split("/")[-1]
    author_block_pattern = re.compile(
        rf'"authorId"\s*:\s*"{re.escape(author_id)}".{{0,4000}}?"citationCount"\s*:\s*(\d+)',
        re.IGNORECASE | re.DOTALL,
    )
    match = author_block_pattern.search(html)
    if match:
        return int(match.group(1))

    generic_patterns = [
        r'"citationCount"\s*:\s*(\d+)',
        r'"citations"\s*:\s*(\d+)',
    ]
    for pattern in generic_patterns:
        match = re.search(pattern, html, re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


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
        print(f"Opening Semantic Scholar page: {AUTHOR_URL}", flush=True)
        page.goto(AUTHOR_URL, wait_until="domcontentloaded", timeout=120000)
        try:
            page.wait_for_load_state("networkidle", timeout=30000)
        except Exception:
            print("networkidle wait timed out, continuing with current DOM", flush=True)
        page.wait_for_timeout(5000)
        body_text = page.locator("body").inner_text()
        html = page.content()
        browser.close()

    text_count = parse_citation_count_from_text(body_text)
    if text_count is not None:
        print(f"Found citation count from rendered text: {text_count}", flush=True)
        return text_count

    html_count = parse_citation_count_from_html(html)
    if html_count is not None:
        print(f"Found citation count from page HTML: {html_count}", flush=True)
        return html_count

    os.makedirs("results", exist_ok=True)
    with open("results/ss_debug_body.txt", "w", encoding="utf-8") as f:
        f.write(body_text)
    with open("results/ss_debug_page.html", "w", encoding="utf-8") as f:
        f.write(html)

    raise RuntimeError(
        "Could not find displayed citation count on Semantic Scholar author page. "
        "Saved debug files to results/ss_debug_body.txt and results/ss_debug_page.html."
    )

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
