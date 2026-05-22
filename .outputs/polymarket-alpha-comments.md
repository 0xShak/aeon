## Summary

Ran the `polymarket-alpha-comments` skill end-to-end for 2026-05-22.

**What I did:**
- Pulled top 100 markets by 24h volume from gamma-api, filtered to non-sports with at least one outcome price in [0.10, 0.90].
- Picked 8 unique events spanning the iran-complex (4), plus mstr/btc, btc spot, wti crude, and us-iran-diplomatic. Additionally pulled comments on events 438327 (iran airspace) and 375597 (hormuz return to normal) as adjacent reads.
- Fetched top-by-reactions + most-recent comments per event, dedup'd, and scored against specificity / plausibility / actionability.

**5 alpha calls surfaced (top across all markets, not per market):**
1. `[contrarian]` @Flat-Waterskiing on mstr sells any btc by june 30 (yes 0.52) — three named signals (strc atm above par, +535 btc may 11, saylor post) in 72h.
2. `[contrarian]` @Neighboring-Longitude on iran closes airspace by may 31 (yes 0.315) — kuwait airspace restricted until may 23.
3. `[contrarian]` @Required-Spit on trump-announces-hormuz-blockade-lifted (yes 0.255) — isw-sourced, names soh-passage as binding red line.
4. `[resolution]` @Innocent-Kid on iran-ceasefire-continues-through-may-24 (yes 0.895) — prior april-22 leg resolved NO on the "both sides must co-announce" rule.
5. `[unverified] [insider]` @Dreary-Marketer on hormuz blockade lifted (yes 0.255) — al hadath sourced, pakistan army chief tripwire.

**Files:**
- `articles/polymarket-alpha-comments-2026-05-22.md` (full report)
- `.pending-notify/polymarket-alpha-2026-05-22.md` (notification queued for post-run delivery — `./notify` directly was blocked by sandbox shell-substitution rules; the pending file is the documented sandbox fallback path that the workflow's post-run step picks up)
- `memory/logs/2026-05-22.md` (appended)

**Follow-ups for tomorrow:** watch @Dreary-Marketer for further al-jazeera/al-hadath-sourced iran updates. pull the prior april-22 ceasefire-extension uma proposal text before the may-24 leg locks in — that's the actionable resolution alpha.
