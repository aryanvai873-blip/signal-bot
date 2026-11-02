import telebot
from telebot import types
from flask import Flask
import threading

# ===== এখানে তোমার বটের টোকেন বসাও =====
BOT_TOKEN = "8740724012:AAEPwE-ugiB-cXjDF-cWBnZ4LMU1dehaYQ8
CHANNEL_ID = "@sl_communty" # তোমার চ্যানেলের username
CHANNEL_LINK = "https://t.me/sl_communty"
SITE_LINK = "https://bdxaryan35.12bajeevip.com/register.html"

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "ARYAN VAI VIP BOT LIVE"

def join_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("1️⃣ Channel Join করো", url=CHANNEL_LINK),
        types.InlineKeyboardButton("2️⃣ Site এ Register করো", url=SITE_LINK),
        types.InlineKeyboardButton("🔄 Check করে Bot Start করো ✅", callback_data="check_join")
    )
    return markup

def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📈 GET SIGNAL", callback_data="get_signal"),
        types.InlineKeyboardButton("📊 MARKET", callback_data="market"),
        types.InlineKeyboardButton("💬 SUPPORT", callback_data="support"),
        types.InlineKeyboardButton("ℹ️ HELP", callback_data="help")
    )
    markup.add(types.InlineKeyboardButton("🎮 GAME LINK", url=SITE_LINK))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"🔥 ARYAN VAI VIP BOT এ স্বাগতম {message.from_user.first_name}!\n\nবট চালু করতে ২টা কাজ করো:\n\n1. Channel @sl_communty তে Join করো\n2. Site এ Register করো\n\nতারপর Check বাটনে ক্লিক করো 👇",
        reply_markup=join_menu()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "check_join":
        try:
            check = bot.get_chat_member(CHANNEL_ID, call.from_user.id)
            if check.status in ['member', 'administrator', 'creator']:
                bot.edit_message_text(
                    "🔥 ARYAN VAI VIP BOT 🔥\n\nWelcome! বট অনলাইন ✅\nনিচ থেকে সিলেক্ট করো:",
                    call.message.chat.id,
                    call.message.message_id,
                    reply_markup=main_menu()
                )
            else:
                bot.answer_callback_query(call.id, "❌ আগে @sl_communty চ্যানেলে Join করো!", show_alert=True)
        except Exception as e:
            print(e)
            bot.answer_callback_query(call.id, "❌ Bot কে চ্যানেলের Admin বানাও নাই!", show_alert=True)

    elif call.data == "get_signal":
        bot.send_message(call.message.chat.id, "📡 ARYAN VAI SIGNAL\n\nPair: USD/JPY\nDirection: UP 🟢\nTime: 1 MIN\n\nConfidence: 95%")

    elif call.data == "market":
        bot.answer_callback_query(call.id, "MARKET: OTC OPEN ✅")
    elif call.data == "support":
        bot.send_message(call.message.chat.id, f"💬 Support: {CHANNEL_LINK}")
    elif call.data == "help":
        bot.send_message(call.message.chat.id, "ℹ️ /start দিয়ে বট শুরু করো")

def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
