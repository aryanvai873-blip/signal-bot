import os, random, datetime
import telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

CHANNEL_LINK = "https://t.me/sl_communty"
SITE_LINK = "https://bdxaryan35.12bajeevip.com/register.html"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("GET REAL SIGNAL", "ABOUT BOT", "MY ID", "HELP", "BACKUP ID")
    txt = f"<b>🔥 ARYAN VAI - AVIATOR VIP BOT 🔥</b>\n\nID: 0424 | ONLINE 🟢\n\nChannel: {CHANNEL_LINK}\nSite: {SITE_LINK}"
    bot.send_message(message.chat.id, txt, parse_mode="HTML", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def all_handler(message):
    txt = (message.text or "").lower()
    if "real signal" in txt:
        target = round(random.uniform(1.35, 5.0), 2)
        # কোনো লিংক নাই, তাই প্রিভিউ আসবে না
        caption = f"✈️ AVIATOR VIP SIGNAL ✈️\n\n🎯 TARGET: {target}x\n🛡️ SAFE: {round(target-0.3,2)}x\n\nID: AV-0424-{random.randint(1000,9999)}"
        bot.send_message(message.chat.id, caption)

bot.infinity_polling()
