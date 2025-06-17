import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    store = {"address": "вул. Івасюка 8"}
    city = "Київ"
    await update.message.reply_text(f"{store['address']} ({city})")

app = ApplicationBuilder().token("7771148571:AAEArj1ZZ_zRnn60UxB2qYKJHA3af80w5Es").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()