import os
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
API = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

TASKS = [
    {
        "name": "Triaba Oman — paid surveys",
        "url": "https://www.triaba.com/om",
        "details": "Oman panel. Listed rewards include PayPal, virtual Visa and Oman retail vouchers; not USDT/TRC20."
    },
    {
        "name": "SurveyTalkers Oman — paid surveys",
        "url": "https://surveytalkers.com/om",
        "details": "Oman-specific panel. Check the reward catalogue and eligibility in your account."
    },
    {
        "name": "Clickworker — microtasks",
        "url": "https://www.clickworker.com/clickworker/",
        "details": "Registration and payout options depend on country/account. Oman access is not guaranteed."
    },
    {
        "name": "ySense — surveys and offers",
        "url": "https://www.ysense.com/",
        "details": "Check Oman registration and payout options shown in your account."
    },
]

def main():
    lines = [
        "💰 Daily free-earning opportunities (Oman)",
        "",
        "These are platform links, not guaranteed jobs or guaranteed income.",
        "Only do tasks that appear in your own account and are available in Oman.",
        ""
    ]
    for i, task in enumerate(TASKS, 1):
        lines += [f"{i}. {task['name']}", task["details"], task["url"], ""]
    lines += [
        "₿ TRC20 note: none of these Oman options is verified here as paying directly in USDT TRC20.",
        "Never pay a deposit or VIP fee. Never share your Telegram token, exchange seed phrase, private key or OTP.",
        "",
        "This bot finds and reports opportunities; it cannot complete identity checks, CAPTCHA or surveys, and cannot guarantee earnings."
    ]
    response = requests.post(API, json={
        "chat_id": CHAT_ID,
        "text": "\n".join(lines),
        "disable_web_page_preview": True
    }, timeout=20)
    response.raise_for_status()
    data = response.json()
    if not data.get("ok"):
        raise RuntimeError(f"Telegram API error: {data}")
    print("Telegram daily earning report sent.")

if __name__ == "__main__":
    main()
