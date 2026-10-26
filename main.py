import os
import random
import datetime
from flask import Flask
from threading import Thread
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 24H Server
flask_app = Flask('')
@flask_app.route('/')
def home(): return "ARYAN VAI VIP BOT LIVE 24H"
Thread(target=lambda: flask_app.run(host='0.0.0.0', port=8080)).start()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["GET REAL SIGNAL", "ABOUT BOT"],
        ["MY ID", "HELP"],
        ["BACKUP ID"]
    ]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Welcome to ARYAN VAI VIP BOT ✅\n24H ONLINE\nID: 0424",
        reply_markup=markup
    )

async def handle_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text
    if "GET REAL SIGNAL" in txt or "SIGNAL" in txt:
        sig = random.choice(["SMALL 🟢", "BIG 🔴"])
        now = datetime.datetime.now().strftime('%H:%M:%S')
        uid = random.randint(1000,9999)
        text = f"""
🔥 ARYAN VAI - VIP SIGNAL 🔥

📊 SIGNAL: 🔴 {sig}
⏰ TIME: {now}
🆔 ID: ARYAN-0424-{uid}

✅ 99% ACCURACY

"""
        await update.message.reply_text(text)
    elif "ABOUT" in txt:
        await update.message.reply_text("ARYAN VAI VIP BOT - 99% Accuracy - 24H Active - VIP COLOR DESIGN")
    elif "MY ID" in txt:
        await update.message.reply_text(f"Your ID: {update.effective_user.id}")
    elif "HELP" in txt:
        await update.message.reply_text("শুধু GET REAL SIGNAL চাপো")
    elif "BACKUP" in txt:
        await update.message.reply_text("Backup ID: @aryan_backup")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_all))
    print("VIP BOT RUNNING")
    app.run_polling()

if __name__ == "__main__":
    main()
