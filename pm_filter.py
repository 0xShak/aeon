#!/usr/bin/env python3
import json
from datetime import datetime, timezone

d = json.load(open('/tmp/pm_markets.json'))
out = []
out.append(f"Total markets: {len(d)}")

now = datetime.now(timezone.utc)

candidates = []
for m in d:
    try:
        op = m.get('outcomePrices', '[]')
        if isinstance(op, str):
            op = json.loads(op)
        if not op or len(op) != 2:
            continue
        p0 = float(op[0])
        p1 = float(op[1])
        liq = float(m.get('liquidityNum') or m.get('liquidity') or 0)
        vol24 = float(m.get('volume24hr') or 0)
        end = m.get('endDate') or m.get('endDateIso')
        if not end:
            continue
        try:
            end_dt = datetime.fromisoformat(end.replace('Z', '+00:00'))
        except Exception:
            continue
        hours_to_end = (end_dt - now).total_seconds() / 3600
        if hours_to_end < 24 or hours_to_end > 24*30:
            continue
        if liq < 10000:
            continue
        if vol24 < 2000:
            continue
        if not (p0 > 0.80 or p0 < 0.20):
            continue
        outcomes_raw = m.get('outcomes')
        try:
            outcomes_parsed = json.loads(outcomes_raw) if isinstance(outcomes_raw, str) else outcomes_raw
        except Exception:
            outcomes_parsed = outcomes_raw
        clob_raw = m.get('clobTokenIds')
        try:
            clob_parsed = json.loads(clob_raw) if isinstance(clob_raw, str) else clob_raw
        except Exception:
            clob_parsed = clob_raw
        ev = (m.get('events') or [{}])[0] if m.get('events') else {}
        candidates.append({
            'question': m.get('question'),
            'slug': m.get('slug'),
            'p0': p0,
            'p1': p1,
            'liquidity': liq,
            'volume24hr': vol24,
            'volume': float(m.get('volume', 0) or 0),
            'endDate': end,
            'hoursToEnd': hours_to_end,
            'outcomes': outcomes_parsed,
            'clobTokenIds': clob_parsed,
            'eventSlug': ev.get('slug'),
            'eventId': ev.get('id'),
            'eventTitle': ev.get('title'),
            'description': (m.get('description') or '')[:500],
        })
    except Exception as e:
        pass

candidates.sort(key=lambda x: x['volume24hr'], reverse=True)
out.append(f"Heavy-favorite candidates: {len(candidates)}")
out.append("")
for i, c in enumerate(candidates[:30]):
    fav_outcome = c['outcomes'][0] if (c['outcomes'] and c['p0'] > 0.5) else (c['outcomes'][1] if c['outcomes'] else '?')
    fav_price = c['p0'] if c['p0'] > 0.5 else c['p1']
    out.append(f"{i+1}. [{fav_price:.3f} {fav_outcome}] {c['question']}")
    out.append(f"   slug={c['slug']} event={c['eventSlug']}")
    out.append(f"   liq=${c['liquidity']:.0f} vol24=${c['volume24hr']:.0f} ends in {c['hoursToEnd']/24:.1f}d ({c['endDate']})")
    out.append(f"   desc: {c['description'][:200]}")
    out.append("")

with open('/home/runner/work/aeon/aeon/pm_filtered.txt', 'w') as f:
    f.write('\n'.join(out))
with open('/home/runner/work/aeon/aeon/pm_candidates.json', 'w') as f:
    json.dump(candidates, f, indent=2)
print("done")
