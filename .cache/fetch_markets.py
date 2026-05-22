#!/usr/bin/env python3
"""Fetch Polymarket markets via HTTP and dump trimmed view."""
import json
import urllib.request
import sys

url = "https://gamma-api.polymarket.com/markets?closed=false&active=true&order=volume24hr&ascending=false&limit=25"
req = urllib.request.Request(url, headers={"User-Agent": "aeon-skill/1.0"})
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.load(r)

with open("/home/runner/work/aeon/aeon/.cache/pm_markets.json", "w") as f:
    json.dump(data, f)

for m in data:
    try:
        vol24 = float(m.get("volume24hr", 0) or 0)
        prices = json.loads(m.get("outcomePrices", "[]"))
        outcomes = json.loads(m.get("outcomes", "[]"))
        category = m.get("category", "") or ""
        question = m.get("question", "")
        slug = m.get("slug", "")
        event_slug = ""
        event_id = ""
        events = m.get("events", [])
        if events and isinstance(events, list):
            event_slug = events[0].get("slug", "")
            event_id = events[0].get("id", "")
        print(f"vol24=${vol24:,.0f} | cat={category[:14]:14s} | px={prices} | {question[:90]} || slug={slug} | event_slug={event_slug} | event_id={event_id}")
    except Exception as e:
        print("ERR", e, m.get("question"))
