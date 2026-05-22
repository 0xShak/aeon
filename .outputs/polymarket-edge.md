## Summary

Ran `polymarket-edge` for 2026-05-22. Scanned top 80 markets by 24h volume, filtered on liquidity/window/price, fetched CLOB price history for the four in-window candidates, then ran a news-baseline check.

**1 edge shipped:**

- **US x Iran permanent peace deal by June 15, 2026?** — SHORT YES @ 0.315, conviction 8/10, resolves 2026-06-15. Fair read 0.12-0.15, gap ~18pp. The framework tabled May 7 mechanically triggers a 30-day technical negotiation window before any signed permanent deal, and Iran is still "reviewing" with an unresolved 15-year delta on the enrichment moratorium (Iran 5y / US 20y).

**Skipped with reasons:** Iran airspace May 24 (gap under 8pp), May 31 peace deal (same trade already shipped yesterday), Hormuz June 30 (20+pp gap on news but 39 days out, outside window).

**Files:**
- `articles/polymarket-edge-2026-05-22.md` (full report with sources)
- `.pending-notify/polymarket-edge-2026-05-22.md` (queued for post-run delivery — direct `./notify` shell invocation blocked in this sandbox)
- `memory/logs/2026-05-22.md` (Polymarket Edge section appended)
- `memory/MEMORY.md` (Open positions table updated with the new 8/10 entry)

**Follow-up:** `prediction-journal` can settle this position when the market resolves on 2026-06-15. Cleanup of `.poly-*` and `.ph-*` temp files was blocked by sandbox rm policy on hidden files — workflow housekeeping should sweep them.

Sources:
- [Iran reviews U.S. peace proposal — CNBC, 2026-05-21](https://www.cnbc.com/2026/05/21/iran-war-us-peace-talks-trump-hormuz.html)
- [U.S. Proposes 20-Year Iran Enrichment Freeze — Defense News](https://www.thedefensenews.com/news-details/US-Proposes-20-Year-Iran-Enrichment-Freeze-in-New-Nuclear-Framework-and-30-Day-Talks-Plan/)
- [US, Iran closing in on one-page memo to end war — Axios, 2026-05-06](https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo)
- [Iran reopens airspace — Al Jazeera](https://www.aljazeera.com/news/2026/1/15/iran-closes-airspace-to-most-flights-amid-threat-of-us-attack-monitors)
- [Strait of Hormuz Commercial Transits at Lowest Level — USNI News](https://news.usni.org/2026/05/01/strait-of-hormuz-commercial-transits-at-lowest-level-since-operation-epic-fury-start-shipping-data-shows)
