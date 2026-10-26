import os
from flask import Flask
import threading
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Render এর Environment থেকে টোকেন নেবে
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Flask - Render কে খুশি রাখার জন্য
flask_app = Flask(__name__)
@flask_app.route('/')
def home():
    return "Bot is Running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host='0.0.0.0', port=port)

async def start(update, context):
    await update.message.reply_text("Hi! ARYAN VAI Bot is Online ✅")

async def reply_all(update, context):
    await update.message.reply_text(f"You said: {update.message.text}")

def run_bot():
    print(f"BOT_TOKEN loaded: {BOT_TOKEN is not None}")
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN is missing in Render Environment!")
        return
    
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_all))
    print("Starting bot polling...")
    app.run_polling()

if __name__ == "__main__":
    # Flask আলাদা thread এ চালাও
    t = threading.Thread(target=run_flask)
    t.start()
    # Bot মেইন thread এ চালাও
    run_bot()
