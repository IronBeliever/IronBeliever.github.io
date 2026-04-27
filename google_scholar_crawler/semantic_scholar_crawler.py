import json
import os
from datetime import datetime

import requests

author_id = os.environ["SEMANTIC_SCHOLAR_AUTHOR_ID"]
api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")

headers = {}
if api_key:
    headers["x-api-key"] = api_key

resp = requests.get(
    f"https://api.semanticscholar.org/graph/v1/author/{author_id}",
    params={"fields": "name,url,citationCount"},
    headers=headers,
    timeout=30,
)
resp.raise_for_status()
author = resp.json()

os.makedirs("results", exist_ok=True)

with open("results/ss_data.json", "w", encoding="utf-8") as f:
    json.dump(
        {
            "name": author.get("name"),
            "updated": str(datetime.now()),
            "citedby": author.get("citationCount", 0),
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
            "message": str(author.get("citationCount", 0)),
        },
        f,
        ensure_ascii=False,
    )
