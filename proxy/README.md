# AI proxy for the portfolio

Lets "ask me" and "check my fit" call Claude from GitHub Pages without putting an API key in the page.

1. Install the Vercel CLI (`npm i -g vercel`), then from this folder run `vercel --prod`.
2. In the Vercel project settings, add the env var `ANTHROPIC_API_KEY` (your own key) and redeploy.
3. Optional env vars: `ALLOWED_ORIGINS` (default `https://limiz6383.github.io`), `DAILY_CAP` (default 150), `MODEL_QUICK`, `MODEL_DEFAULT`.
4. Copy the deployed URL (like `https://your-proxy.vercel.app/api/ai`) into `AI_PROXY` near the top of the page script in `index.html`, then commit.

Set a monthly spend limit on the key in the Anthropic Console as the real safety net; the limits in this file are best-effort only.
