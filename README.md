# Free Oman Earning Alert Bot

A GitHub Actions bot that sends a daily Telegram message with free earning-platform links relevant to Oman.

## What it does
- Sends a daily opportunity list to Telegram at about 14:00 Oman time.
- Can also be run manually from the Actions tab.
- Flags country and payout uncertainty.

## Important limits
- This is an opportunity finder/alert, not an automatic worker. It cannot complete surveys, identity checks or CAPTCHA, and it cannot guarantee income.
- No listed platform is verified here as paying directly in USDT TRC20. Triaba Oman lists PayPal, virtual Visa and local retail vouchers. Check each platform's own account payout page before doing work.
- Never pay registration, deposit or VIP fees. Never give the bot an exchange seed phrase or private key.

## Setup (mobile-friendly)
1. In Telegram, open your bot, press **Start**, and send it a message.
2. In a browser, open `https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates` (replace the placeholder privately with your BotFather token). Find `message.chat.id`. Do not share this URL or token with anyone. If updates are empty, send another message to the bot and refresh.
3. In this GitHub repository open **Settings → Secrets and variables → Actions → New repository secret**.
4. Add:
   - `TELEGRAM_BOT_TOKEN` = token from BotFather
   - `TELEGRAM_CHAT_ID` = numeric chat ID from getUpdates
5. Open **Actions → Daily Oman earning report → Run workflow** to test. Enable Actions if GitHub asks.
6. The report is scheduled daily at 14:00 Oman time.

Do not paste your bot token into chat, issues, commits or public files. If it was exposed, revoke it with BotFather and create a new one.
