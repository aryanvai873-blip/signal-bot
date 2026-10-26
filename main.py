import os
import random
import telebot
from telebot import types
from flask import Flask
import threading

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "ARYAN VAI Bot Live"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("📈 GET SIGNAL", callback_data="signal")
    btn2 = types.InlineKeyboardButton("📊 MARKET", callback_data="market")
    btn3 = types.InlineKeyboardButton("💬 SUPPORT", callback_data="support")
    btn4 = types.InlineKeyboardButton("ℹ️ HELP", callback_data="help")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    bot.send_message(message.chat.id, "🔥 *ARYAN VAI VIP BOT* 🔥\n\nWelcome! বট অনলাইন ✅\nনিচ থেকে সিলেক্ট করো:", parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "signal":
        pairs = ["EUR/USD", "GBP/USD", "USD/JPY", "BTC/USD", "EUR/JPY"]
        pair = random.choice(pairs)
        direction = random.choice(["UP 🟢", "DOWN 🔴"])
        m = types.InlineKeyboardMarkup()
        m.add(types.InlineKeyboardButton("📈 NEXT SIGNAL", callback_data="signal"))
        bot.send_message(call.message.chat.id, f"📡 *SIGNAL*\n\nPair: `{pair}`\nDir: *{direction}*\nTime: 1 MIN", parse_mode="Markdown", reply_markup=m)
    elif call.data == "market":
        bot.send_message(call.message.chat.id, "📊 OTC Market Active ✅")
    elif call.data == "support":
        bot.send_message(call.message.chat.id, "Support: @ARYAN_VAI")
    elif call.data == "help":
        bot.send_message(call.message.chat.id, "Help: /start দাও")

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    print(f"BOT_TOKEN loaded: {bool(BOT_TOKEN)}")
    print("Starting bot polling...")
    bot.infinity_polling()
