#!/usr/bin/env python3
import json
from datetime import datetime, timezone

data = json.load(open('.pm_markets.json'))
print(f"Total markets: {len(data)}")
print()

now = datetime.now(timezone.utc)

def parse_date(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace('Z', '+00:00'))
    except Exception:
        return None

def safe_json(s):
    if not s:
        return None
    if isinstance(s, list):
        return s
    try:
        return json.loads(s)
    except Exception:
        return None

results = []
for m in data:
    mid = m.get('id')
    q = m.get('question', '')
    slug = m.get('slug', '')
    vol24 = float(m.get('volume24hr') or 0)
    liq = float(m.get('liquidityNum') or 0)
    end = parse_date(m.get('endDate'))
    prices = safe_json(m.get('outcomePrices'))
    outcomes = safe_json(m.get('outcomes'))
    yes_price = None
    if prices and len(prices) >= 1:
        try:
            yes_price = float(prices[0])
        except Exception:
            pass
    hrs_to_end = None
    if end:
        hrs_to_end = (end - now).total_seconds() / 3600
    results.append({
        'id': mid,
        'q': q,
        'slug': slug,
        'vol24': vol24,
        'liq': liq,
        'end': end.isoformat() if end else None,
        'hrs': hrs_to_end,
        'yes': yes_price,
        'outcomes': outcomes,
    })

# Print summary
for r in results:
    print(f"[{r['vol24']:>12,.0f}] yes={r['yes']} liq={r['liq']:,.0f} hrs={r['hrs']:.0f if r['hrs'] is not None else '?'} | {r['q'][:80]}")
    print(f"    slug={r['slug']}")
