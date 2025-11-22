import imaplib
import email
import time
import asyncio
from telegram import Bot

# --- TELEGRAM SETUP ---
TELEGRAM_BOT_TOKEN = "8382170415:AAF07cbDd90SRqYFs4teAcelQsMvDeMCmLc"
CHAT_ID = 8037947335

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# --- GMAIL SETUP ---
GMAIL_USER = "ravindrakumawat872@gmail.com"
GMAIL_APP_PASSWORD = "sabp wnrr lctc onui"

async def send_telegram(text):
    await bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

def read_email():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(GMAIL_USER, GMAIL_APP_PASSWORD)
    mail.select("inbox")

    result, data = mail.search(None, "UNSEEN")
    mail_ids = data[0].split()

    messages = []

    for num in mail_ids:
        _, msg_data = mail.fetch(num, "(RFC822)")
        raw = msg_data[0][1]
        msg = email.message_from_bytes(raw)

        subject = msg["subject"]

        if msg.is_multipart():
            body = msg.get_payload(0).get_payload()
        else:
            body = msg.get_payload()

        text = f"📩 *New Email Alert*\n\n*Subject:* {subject}\n\n*Message:* {body}"
        messages.append(text)

    mail.close()
    mail.logout()

    return messages

async def main_loop():
    print("✔ Email → Telegram Alert System is running…")

    while True:
        msgs = read_email()

        for m in msgs:
            await send_telegram(m)

        await asyncio.sleep(5)

asyncio.run(main_loop())
 