import os, random, telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

CHANNEL_LINK = "https://t.me/sl_communty"
SITE_LINK = "https://bdxaryan35.12bajeevip.com/register.html"
SUPPORT_LINK = "https://t.me/SIGNAL_MASTERVI1"

# তোমার Aviator ছবির Direct Link - এইটা 100% কাজ করবে
PHOTO_URL = "https://i.ibb.co/KpMpky8Y/aviator.jpg" 
# যদি না হয়, তাহলে তোমার ibb লিংক https://ibb.co/KpMpky8Y ওপেন করে Right Click > Copy Image Address বসাও

@bot.message_handler(commands=['start'])
def start(msg):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🚀 GET REAL SIGNAL")
    bot.send_message(msg.chat.id, "🔥 VIP BOT ONLINE 🟢\nনিচে চাপ দাও", reply_markup=kb)

@bot.message_handler(func=lambda m: m.text and "GET REAL SIGNAL" in m.text)
def get_signal(msg):
    main = round(random.uniform(4.20, 9.80), 2)
    safe1 = round(main * 0.65, 2)
    safe2 = round(main - 0.40, 2)

    caption = (
        f"✈️ AVIATOR VIP SIGNAL\n\n"
        f"🎯 TARGET : {main}x\n"
        f"🛡️ SAFE 1 : {safe1}x\n"
        f"🛡️ SAFE 2 : {safe2}x\n\n"
        f"⏳ STATUS : PENDING..."
    )

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📢 Channel Join", url=CHANNEL_LINK),
        types.InlineKeyboardButton("🌐 Official Site", url=SITE_LINK)
    )
    markup.add(
        types.InlineKeyboardButton("💬 Support", url=SUPPORT_LINK),
        types.InlineKeyboardButton("🎁 Bonus Claim", url=SITE_LINK)
    )
    markup.add(
        types.InlineKeyboardButton("▶️ Play Now Aviator", url=SITE_LINK)
    )

    # ছবি + ক্যাপশন একসাথে পাঠাবে
    bot.send_photo(msg.chat.id, photo=PHOTO_URL, caption=caption, reply_markup=markup)

print("BOT RUNNING - PHOTO MODE")
bot.infinity_polling()
