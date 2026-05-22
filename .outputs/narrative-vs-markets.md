## Summary

Executed the `narrative-vs-markets` skill for 2026-05-22.

**What I did:**
- Scanned ~120 top Polymarket markets by 24h volume, filtered to the 2-day-to-45-day resolution window
- Picked 6 candidates spanning Iran complex, BTC, NBA, Fed
- Pulled current price + 24h/7d deltas via CLOB price-history API (XAI x_search blocked in sandbox; used WebSearch for narrative reads — flagged in the article)
- Computed gap = |twitter_implied − market_implied|, kept gaps ≥15pp
- Shipped 3 gaps, all same shape: **ct loud, tape right**
  - **US x Iran peace deal by May 31** — gap 47pp (twitter ~0.65 vs market 0.185)
  - **Iranian regime fall by June 30** — gap 25pp (twitter ~0.30 vs market 0.045)
  - **Hormuz traffic normal by end of June** — gap 25pp (twitter ~0.55 vs market 0.305)

**Files:**
- `articles/narrative-vs-markets-2026-05-22.md` — full report with sources
- `.pending-notify/narrative-vs-markets-2026-05-22.md` — queued notification (1,359 chars; sandbox blocked direct `./notify` invocation, post-run step delivers it)
- `memory/logs/2026-05-22.md` — appended log entry

**Follow-up:** add a `narrative-vs-markets` case to `scripts/prefetch-xai.sh` so future runs get real x_search density per market question. Today's narrative pull was qualitative via WebSearch, defensible but coarser than the skill specifies.
