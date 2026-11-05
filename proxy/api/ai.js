// Tiny Vercel serverless proxy so the portfolio's "ask me" and "check my fit" can call Claude
// from GitHub Pages without exposing an API key. Set ANTHROPIC_API_KEY in Vercel's env vars.
const ALLOWED = (process.env.ALLOWED_ORIGINS || 'https://limiz6383.github.io').split(',');
const MODELS = {
  quick: process.env.MODEL_QUICK || 'claude-haiku-5-5',
  default: process.env.MODEL_DEFAULT || 'claude-sonnet-5-5',
};
const MAX_PROMPT = 14000;      // characters accepted per request
const MAX_TOKENS = 1200;       // cap on reply length
const PER_IP_PER_HOUR = 20;    // best-effort limit (per warm instance)
const DAILY_CAP = Number(process.env.DAILY_CAP || 150); // best-effort total calls per day per instance
const hits = new Map();
let day = new Date().toISOString().slice(0, 10), dayCount = 0;

module.exports = async (req, res) => {
  const origin = req.headers.origin || '';
  const ok = ALLOWED.includes(origin);
  res.setHeader('Vary', 'Origin');
  if (ok) {
    res.setHeader('Access-Control-Allow-Origin', origin);
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  }
  if (req.method === 'OPTIONS') return res.status(ok ? 204 : 403).end();
  if (!ok) return res.status(403).json({ error: 'forbidden_origin' });
  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });

  const today = new Date().toISOString().slice(0, 10);
  if (today !== day) { day = today; dayCount = 0; hits.clear(); }
  const ip = (req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'unknown';
  const now = Date.now();
  const recent = (hits.get(ip) || []).filter(t => now - t < 3600e3);
  if (recent.length >= PER_IP_PER_HOUR || dayCount >= DAILY_CAP) return res.status(429).json({ error: 'rate_limited' });
  recent.push(now); hits.set(ip, recent); dayCount++;

  const body = typeof req.body === 'string' ? JSON.parse(req.body || '{}') : (req.body || {});
  const prompt = String(body.prompt || '');
  if (!prompt || prompt.length > MAX_PROMPT) return res.status(400).json({ error: 'bad_prompt' });
  const model = MODELS[body.tier === 'quick' ? 'quick' : 'default'];

  try {
    const r = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'x-api-key': process.env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01',
      },
      body: JSON.stringify({ model, max_tokens: MAX_TOKENS, messages: [{ role: 'user', content: prompt }] }),
    });
    const j = await r.json();
    if (!r.ok) return res.status(502).json({ error: 'upstream', status: r.status });
    const text = (j.content || []).map(c => c.text || '').join('');
    return res.status(200).json({ text });
  } catch (e) {
    return res.status(502).json({ error: 'upstream_failed' });
  }
};
