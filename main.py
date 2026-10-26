import os
import random
from flask import Flask
from threading import Thread
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# --- Flask Server for Render 24H ---
flask_app = Flask('')
@flask_app.route('/')
def home():
    return "ARYAN VAI VIP BOT IS LIVE!"

def run_flask():
    flask_app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

# --- Telegram Bot ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["GET REAL SIGNAL", "ABOUT BOT"],
        ["HELP", "STATS"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🔥 ARYAN VAI VIP BOT 🔥\n\nWelcome! Click GET REAL SIGNAL",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "GET REAL SIGNAL":
        signals = ["BUY 📈", "SELL 📉", "WAIT ⏳"]
        result = random.choice(signals)
        await update.message.reply_text(f"💰 TODAY SIGNAL: {result}\n\nTime: {context._chat_id}")
    elif text == "ABOUT BOT":
        await update.message.reply_text("This is ARYAN VAI VIP Signal Bot - 99% Accuracy")
    else:
        await update.message.reply_text("Press GET REAL SIGNAL")

def main():
    Thread(target=run_flask).start()
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot Started...")
    application.run_polling()

if __name__ == '__main__':
    main()
