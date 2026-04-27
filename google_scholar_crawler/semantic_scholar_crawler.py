import json
import os
from datetime import datetime

import requests

author_id = os.environ["SEMANTIC_SCHOLAR_AUTHOR_ID"]
api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")

manual_file = os.path.join(os.path.dirname(__file__), "ss_manual_citations.json")

headers = {}
if api_key:
    headers["x-api-key"] = api_key


def load_manual_citation_count() -> int:
    if not os.path.exists(manual_file):
        return 0

    with open(manual_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    return int(data.get("manual_citation_count", 0))


resp = requests.get(
    f"https://api.semanticscholar.org/graph/v1/author/{author_id}",
    params={"fields": "name,url,citationCount"},
    headers=headers,
    timeout=30,
)
resp.raise_for_status()
author = resp.json()

api_count = int(author.get("citationCount", 0))
manual_count = load_manual_citation_count()
final_count = max(api_count, manual_count)

os.makedirs("results", exist_ok=True)

with open("results/ss_data.json", "w", encoding="utf-8") as f:
    json.dump(
        {
            "name": author.get("name"),
            "updated": str(datetime.now()),
            "citedby": final_count,
            "api_citedby": api_count,
            "manual_citedby": manual_count,
            "url": author.get("url"),
        },
        f,
        ensure_ascii=False,
    )

with open("results/ss_data_shieldsio.json", "w", encoding="utf-8") as f:
    json.dump(
        {
            "schemaVersion": 1,
            "label": "Semantic Scholar",
            "message": str(final_count),
        },
        f,
        ensure_ascii=False,
    )
