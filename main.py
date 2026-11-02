import telebot
from telebot import types
from flask import Flask
import threading
import os

BOT_TOKEN = "8740724012:AAEPwE-ugiB-cXjDF-cWBnZ4LMU1dehaYQ8"
CHANNEL_ID = "@sl_communty"
CHANNEL_LINK = "https://t.me/sl_communty"
SITE_LINK = "https://bdxaryan35.12bajeevip.com/register.html"

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(name)

@app.route('/')
def home()
    return "ARYAN VAI VIP BOT LIVE"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("1️⃣ Channel Join করো", url=CHANNEL_LINK),
        types.InlineKeyboardButton("2️⃣ Site এ Register করো", url=SITE_LINK),
        types.InlineKeyboardButton("🔄 Check করে Bot Start করো ✅", callback_data="check_join")
    )
    bot.send_message(message.chat.id, f"🔥 ARYAN VAI VIP BOT চালু করতে ২টা কাজ করো:\n\n1. Channel @sl_communty তে Join করো\n2. Site এ Register করো\n\nতারপর Check বাটনে ক্লিক করো 👇", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def check(call):
    if call.data == "check_join":
        try:
            m = bot.get_chat_member(CHANNEL_ID, call.from_user.id)
            if m.status in ['member','administrator','creator']:
                mk = types.InlineKeyboardMarkup(row_width=2)
                mk.add(types.InlineKeyboardButton("📈 GET SIGNAL", callback_data="sig"), types.InlineKeyboardButton("📊 MARKET", callback_data="mkt"))
                mk.add(types.InlineKeyboardButton("🎮 GAME LINK", url=SITE_LINK))
                bot.send_message(call.message.chat.id, "✅ ভেরিফাইড! Welcome!\n🔥 ARYAN VAI VIP BOT 🔥", reply_markup=mk)
            else:
                bot.answer_callback_query(call.id, "❌ আগে @sl_communty তে Join করো!", show_alert=True)
        except:
            bot.answer_callback_query(call.id, "❌ Bot কে চ্যানেলে Admin বানাও!", show_alert=True)
    elif call.data == "sig":
        bot.send_message(call.message.chat.id, "📡 SIGNAL: USD/JPY UP 🟢 1 MIN")

def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot).start()
app.run(host='0.0.0.0', port=8080)
