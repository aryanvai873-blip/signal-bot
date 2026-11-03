import os, random, telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN") or "PASTE_YOUR_TOKEN_HERE"
bot = telebot.TeleBot(BOT_TOKEN)

# তোমার সব ফাইনাল লিংক
CHANNEL_LINK = "https://t.me/sl_communty"
SITE_LINK = "https://bdxaryan35.12bajeevip.com/register.html"
SUPPORT_LINK = "https://t.me/SIGNAL_MASTERVI1"

# তোমার ছবি - ডাইরেক্ট লিংক
PHOTO_URL = "https://i.ibb.co/KpMpky8Y/aviator-signal.jpg"  # <-- এখানে Copy Image Address এর লিংক বসাও
# যদি কাজ না করে তাহলে এইটা ব্যবহার করো: https://ibb.co/KpMpky8Y এর ভিতরের ডাইরেক্ট লিংক

@bot.message_handler(commands=['start'])
def start(msg):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🚀 GET REAL SIGNAL")
    bot.send_message(msg.chat.id, "🔥 VIP AVIATOR BOT ONLINE 🟢", reply_markup=kb)

@bot.message_handler(func=lambda m: "GET REAL SIGNAL" in m.text)
def signal(msg):
    t = round(random.uniform(4.50, 9.20), 2)
    s1 = round(t*0.65, 2)
    s2 = round(t-0.40, 2)
    
    caption = f"✈️ VIP SIGNAL\n\n🎯 MAIN : {t}x\n🛡️ SAFE 1 : {s1}x\n🛡️ SAFE 2 : {s2}x\n\n⏳ STATUS : PENDING..."

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
        types.InlineKeyboardButton("▶️ Play Now", url=SITE_LINK)
    )
    
    bot.send_photo(msg.chat.id, photo=PHOTO_URL, caption=caption, reply_markup=markup)

bot.infinity_polling()
