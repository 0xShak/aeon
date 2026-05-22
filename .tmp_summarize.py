import json
from datetime import datetime, timezone

with open('.tmp_pm_markets.json') as f:
    markets = json.load(f)

now = datetime.now(timezone.utc)
print(f"Total: {len(markets)}")
print(f"Now: {now.isoformat()}\n")

for i, m in enumerate(markets):
    try:
        prices = json.loads(m.get('outcomePrices') or '[]')
        outcomes = json.loads(m.get('outcomes') or '[]')
        liq = float(m.get('liquidityNum') or 0)
        v24 = float(m.get('volume24hr') or 0)
        end_iso = m.get('endDate', '')
        try:
            end_dt = datetime.fromisoformat(end_iso.replace('Z', '+00:00'))
            days_to_end = (end_dt - now).total_seconds() / 86400
        except Exception:
            days_to_end = -999
        slug = m.get('slug', '')[:70]
        q = (m.get('question') or '')[:80]
        print(f"[{i}] slug={slug}")
        print(f"    Q: {q}")
        print(f"    outcomes={outcomes}  prices={prices}")
        print(f"    liq=${liq:,.0f}  v24=${v24:,.0f}  ends_in={days_to_end:.1f}d  end={end_iso}")
        print(f"    eventSlug={m.get('events',[{}])[0].get('slug','') if m.get('events') else ''}  category={m.get('category','')}")
        print()
    except Exception as e:
        print(f"[{i}] ERR: {e} slug={m.get('slug')}")
