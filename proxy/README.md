# AI proxy for the portfolio

Lets "check my fit" and "ask me" call Claude from the GitHub Pages site without putting an API key in the page. The key lives only in Vercel's environment settings.

## Deploy (about 5 minutes, free Vercel account is fine)

1. Go to vercel.com, sign in with GitHub, click **Add New > Project**, and import `limiz6383/limiz6383.github.io`.
2. In **Root Directory** choose `proxy`. Leave everything else as is.
3. Open **Environment Variables**, add `ANTHROPIC_API_KEY` with your key (create one at console.anthropic.com > API keys), then click **Deploy**.
4. Visit `https://YOUR-PROJECT.vercel.app/api/ai` in a browser. You should see `{"ok":true,"keySet":true,...}`.
5. Send that URL to Claude (or paste it into `AI_PROXY` near the top of the page script in `index.html` and commit). The page then uses it automatically.

## Safety

- In the Anthropic Console, set a **monthly spend limit** on this key. That is the real safety net.
- The proxy only accepts requests from `https://limiz6383.github.io`, caps prompt size and reply length, and rate-limits per visitor and per day (best-effort, per warm instance).
- Optional env vars: `ALLOWED_ORIGINS` (comma-separated), `DAILY_CAP` (default 150), `MODEL_QUICK`, `MODEL_DEFAULT`.
- If the key ever leaks, delete it in the Console and create a new one; nothing else changes.
