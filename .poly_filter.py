import json, sys, time
from datetime import datetime, timezone, timedelta

with open('.poly-top30.json') as f:
    markets = json.load(f)

print(f"Total markets: {len(markets)}")
if markets:
    print("Fields:", list(markets[0].keys()))
    print()
    print("First market sample:")
    m0 = markets[0]
    for k, v in m0.items():
        s = str(v)
        if len(s) > 200:
            s = s[:200] + '...'
        print(f"  {k}: {s}")
