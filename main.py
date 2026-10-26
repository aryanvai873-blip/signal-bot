import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

flask_app = Flask('')
@flask_app.route('/')
def home():
    return "ARYAN VAI VIP BOT IS LIVE!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 ARYAN VAI VIP BOT LIVE! ✅ /start kaj korche")

def run_flask():
    flask_app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

if __name__ == '__main__':
    # Flask background e
    Thread(target=run_flask).start()
    
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN missing!")
    else:
        print("Starting bot...")
        app = Application.builder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.run_polling()
