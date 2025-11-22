from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8382170415:AAF07cbDd90SRqYFs4teAcelQsMvDeMCmLc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is now active! 👍")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Received a message in Telegram!")
    await update.message.reply_text("Bot is now active! 👍")
