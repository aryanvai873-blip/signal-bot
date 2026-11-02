import os, random, datetime
import telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

CHANNEL_LINK = "https://t.me/sl_communty"
SITE_LINK = "https://bdxaryan35.12bajeevip.com/register.html"
MAIN_USERNAME = "@ARYAN_VAI12"
SECOND_USERNAME = "@TRADER_TAHMID_VAI"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("GET REAL SIGNAL", "ABOUT BOT", "MY ID", "HELP", "BACKUP ID")
    txt = f"<b>🔥 ARYAN VAI - AVIATOR VIP BOT 🔥</b>\n\nID: 0424 | ONLINE 🟢\n\n<b>Channel:</b> {CHANNEL_LINK}\n<b>Site:</b> {SITE_LINK}\n\nনিচ থেকে বাটনে ক্লিক করো 👇"
    bot.send_message(message.chat.id, txt, parse_mode="HTML", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def all_handler(message):
    txt = (message.text or "").lower()
    chat_id = message.chat.id
    
    if "real signal" in txt:
        # Low-Risk: 1.20x - 1.55x এর মধ্যে
        target = round(random.uniform(1.20, 1.55), 2)
        safe = round(target - 0.15, 2)
        signal_id = random.randint(1000, 9999)
        now = datetime.datetime.now().strftime("%H:%M:%S")

        caption = (
            f"✈️ <b>AVIATOR VIP SIGNAL</b> ✈️\n\n"
            f"🎯 <b>TARGET: {target}x</b>\n"
            f"🛡️ <b>SAFE: {safe}x</b>\n\n"
            f"🆔 <b>ID:</b> AV-0424-{signal_id}\n"
            f"⏰ <b>TIME:</b> {now}\n\n"
            f"⏳ <b>STATUS: PENDING...</b>\n"
            f"<i>Waiting for next round</i>"
        )
        # কোনো লিংক নাই, তাই প্রিভিউ আসবে না
        bot.send_message(chat_id, caption, parse_mode="HTML")

    elif "about" in txt:
        bot.send_message(chat_id, "<b>ABOUT:</b> VIP BOT ID 0424 - Low Risk Mode", parse_mode="HTML")
    elif "my id" in txt:
        bot.send_message(chat_id, f"<b>YOUR ID:</b> <code>{message.from_user.id}</code>", parse_mode="HTML")
    elif "help" in txt:
        bot.send_message(chat_id, f"<b>MAIN ID:</b> {MAIN_USERNAME}", parse_mode="HTML")
    elif "backup" in txt:
        bot.send_message(chat_id, f"<b>BACKUP ID:</b> {SECOND_USERNAME}", parse_mode="HTML")

print("LOW-RISK BOT WITH PENDING RUNNING")
bot.infinity_polling()
