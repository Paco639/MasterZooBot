from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Твоя база магазинів – заглушка (тут встав реальну логіку пошуку)
def find_store_by_text(text: str) -> str:
    if "Івасюка" in text:
        return "Івасюка 8 – навпроти кас Новус | 066-188-49-07"
    return "Магазин не знайдено за вашим запитом."

# Обробник команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Напиши адресу або назву вулиці, я знайду магазин MasterZoo")

# Обробник усіх повідомлень
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
result = find_store_by_text(query)
    await update.message.reply_text(result)

def main():
    app = ApplicationBuilder().token("7771148571:AAEArj1ZZ_zRnn60UxB2qYKJHA3af80w5Es").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
