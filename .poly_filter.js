const fs = require('fs');
const markets = JSON.parse(fs.readFileSync('.poly-top80.json', 'utf8'));

// Today (per CLAUDE.md): 2026-05-22. Use late-morning UTC anchor.
const now = new Date('2026-05-22T14:00:00Z');
const minEnd = new Date(now.getTime() + 12 * 3600 * 1000); // 12h from now
const maxEnd = new Date(now.getTime() + 30 * 86400 * 1000); // 30d from now

console.log(`Top ${markets.length} markets by 24h volume:`);
console.log('idx | vol24    | liq      | end        | YES   | NO    | pass | question');
console.log('-'.repeat(140));

const candidates = [];
markets.forEach((m, i) => {
  const v24 = m.volume24hr || 0;
  const liq = m.liquidityNum || m.liquidity || 0;
  const end = m.endDateIso || m.endDate;
  const endDate = end ? new Date(end) : null;
  let prices = [];
  try { prices = JSON.parse(m.outcomePrices || '[]').map(Number); } catch (e) {}
  let outcomes = [];
  try { outcomes = JSON.parse(m.outcomes || '[]'); } catch (e) {}
  let tokenIds = [];
  try { tokenIds = JSON.parse(m.clobTokenIds || '[]'); } catch (e) {}

  const yesPrice = prices[0] !== undefined ? prices[0] : null;
  const noPrice = prices[1] !== undefined ? prices[1] : null;
  const liquidityOk = liq > 5000;
  const volOk = v24 > 2000;
  const inWindow = endDate && endDate >= minEnd && endDate <= maxEnd;
  // "At least one YES price in [0.10, 0.90]" — for binary, check both
  const priceOk = prices.some(p => p >= 0.10 && p <= 0.90);
  const pass = liquidityOk && volOk && inWindow && priceOk;

  const passMark = pass ? 'KEEP' : (
    !liquidityOk ? 'liq' :
    !volOk ? 'vol' :
    !inWindow ? (endDate ? (endDate < minEnd ? 'past' : 'far') : 'noend') :
    !priceOk ? 'edge' : '?'
  );

  console.log(`${i.toString().padStart(2)} | $${Math.round(v24).toLocaleString().padStart(8)} | $${Math.round(liq).toLocaleString().padStart(8)} | ${(end||'-').slice(0,10)} | ${(yesPrice!==null?yesPrice.toFixed(3):'?').padStart(5)} | ${(noPrice!==null?noPrice.toFixed(3):'?').padStart(5)} | ${passMark.padEnd(4)} | ${(m.question||'').slice(0,80)}`);

  if (pass) {
    candidates.push({
      idx: i,
      id: m.id,
      slug: m.slug,
      question: m.question,
      yesPrice,
      noPrice,
      prices,
      outcomes,
      tokenIds,
      v24,
      liq,
      end: end?.slice(0,10),
      conditionId: m.conditionId,
    });
  }
});

console.log(`\nCandidates passing filter: ${candidates.length}`);
fs.writeFileSync('.poly-candidates.json', JSON.stringify(candidates, null, 2));
console.log('Wrote .poly-candidates.json');
