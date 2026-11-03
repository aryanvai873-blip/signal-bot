import os
import random
import datetime
import telebot
from telebot import types

# BOT TOKEN - Render এর জন্য env থেকে নিবে, Pydroid এর জন্য এখানে বসাতে পারবে
BOT_TOKEN = os.getenv("BOT_TOKEN") or "PASTE_YOUR_TOKEN_HERE"
bot = telebot.TeleBot(BOT_TOKEN)

# তোমার ছবির মতো History
HISTORY = [
    "1.29x", "5.20x", "1.12x", "3.07x", "4.17x",
    "1.03x", "13.17x", "1.73x", "2.19x", "6.52x",
    "2.90x", "1.66x", "1.38x", "2.52x", "8.14x", "1.65x"
]

# তোমার সব চ্যানেল - ঘুরে ঘুরে আসবে
CHANNELS = [
    "https://t.me/ARYAN_VAI12",
    "https://t.me/ARYAN_VAI12",
    "https://t.me/ARYAN_VAI12"
]

SITE_LINK = "https://bdxaryan.com"

@bot.message_handler(commands=['start'])
def start(msg):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    kb.add(types.KeyboardButton("🚀 GET REAL SIGNAL"))
    bot.send_message(
        msg.chat.id,
        "🔥 <b>ARYAN VIP - AVIATOR BIG SIGNAL</b> 🔥\n\n"
        "তোমার ছবির মতো History সহ সিগন্যাল পেতে নিচের বাটনে চাপ দাও 👇",
        parse_mode="HTML",
        reply_markup=kb
    )

@bot.message_handler(func=lambda m: m.text and "GET REAL SIGNAL" in m.text)
def get_signal(msg):
    # History + Target
    history_show = " | ".join(random.sample(HISTORY, 7))
    target = round(random.uniform(2.50, 8.50), 2)
    safe1 = round(target * 0.65, 2)
    safe2 = round(target - 0.40, 2)
    signal_id = random.randint(10000, 99999)
    time_now = datetime.datetime.now().strftime("%I:%M:%S %p")
    channel_link = random.choice(CHANNELS)

    caption = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"✈️ <b>AVIATOR VIP BIG SIGNAL</b> ✈️\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📊 <b>ROUND HISTORY</b>\n"
        f"<code>{history_show}</code>\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🚀 <b>CURRENT FLYING : 2.07x</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎯 <b>MAIN TARGET : {target}x</b>\n"
        f"🛡️ SAFE 1 : {safe1}x\n"
        f"🛡️ SAFE 2 : {safe2}x\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🆔 ID : AV-0424-{signal_id}\n"
        f"⏰ TIME : {time_now}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"⏳ <b>STATUS : PENDING...</b>\n"
        f"<i>Waiting For Next Round</i>"
    )

    # 5 টা বাটন সুন্দর করে
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📢 Channel Join", url=channel_link),
        types.InlineKeyboardButton("🌐 Official Site", url=SITE_LINK)
    )
    markup.add(
        types.InlineKeyboardButton("💬 Support", url="https://t.me/ARYAN_VAI12"),
        types.InlineKeyboardButton("🎁 Bonus Claim", url=SITE_LINK)
    )
    markup.add(
        types.InlineKeyboardButton("▶️ Play Now Aviator", url=SITE_LINK)
    )

    bot.send_message(msg.chat.id, caption, parse_mode="HTML", reply_markup=markup)

print("BOT RUNNING - READY")
bot.infinity_polling()
