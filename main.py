import os, random, datetime
from flask import Flask
from threading import Thread
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# --- এখানে তোমার VIP কোড বসাবা ---
VIP_CODE = "ARYAN-VIP-0424"  # এইটা চেঞ্জ করে তোমার কোড বসাও
MAIN_USERNAME = "@ARYAN_VAI12"
SECOND_USERNAME = "@TRADER_TAHMID_VAI"

flask_app = Flask('')
@flask_app.route('/')
def home():
    return "ARYAN VAI VIP BOT IS LIVE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [["GET REAL SIGNAL", "ABOUT BOT"], ["MY ID", "HELP", "BACKUP ID"]]
    markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text("<b>Welcome to ARYAN VAI BOT</b>\nID: 0424\nStatus: ONLINE", parse_mode="HTML", reply_markup=markup)

async def all_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text or ""
    if "REAL SIGNAL" in txt:
        sig = random.choice(["BIG", "SMALL"])
        color = "🟢" if sig == "BIG" else "🔴"
        msg = f"""<b>━━━━━━━━━━━━━━━━━━</b>
<b>🔥 ARYAN VAI - VIP SIGNAL 🔥</b>
<b>━━━━━━━━━━━━━━━━━━</b>
<b>📊 SIGNAL: {color} {sig}</b>
<b>⏰ TIME:</b> {datetime.datetime.now().strftime('%H:%M:%S')}
<b>🆔 ID:</b> <code>ARYAN-0424-{random.randint(1000,9999)}</code>
<b>━━━━━━━━━━━━━━━━━━</b>
<b>✅ 99% ACCURACY | VIP: {VIP_CODE}</b>
<b>━━━━━━━━━━━━━━━━━━</b>"""
        await update.message.reply_text(msg, parse_mode="HTML")
    elif "ABOUT" in txt:
        await update.message.reply_text(f"<b>🤖 ARYAN VAI BOT</b>\n<b>VIP CODE:</b> {VIP_CODE}", parse_mode="HTML")
    elif "MY ID" in txt:
        await update.message.reply_text(f"<b>YOUR ID:</b> <code>{update.effective_user.id}</code>", parse_mode="HTML")
    elif "HELP" in txt:
        await update.message.reply_text(f"<b>MAIN SUPPORT:</b> {MAIN_USERNAME}", parse_mode="HTML")
    elif "BACKUP" in txt:
        await update.message.reply_text(f"<b>BACKUP SUPPORT:</b> {SECOND_USERNAME}", parse_mode="HTML")

def run_flask():
    flask_app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    Thread(target=run_flask).start()
    if BOT_TOKEN:
        app = Application.builder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, all_msg))
        app.run_polling()
