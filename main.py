import random, datetime
import telebot
from telebot import types

BOT_TOKEN = "8300000000:AAH_YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(BOT_TOKEN)

HISTORY = ["1.29x","5.20x","1.12x","3.07x","4.17x","1.03x","13.17x","1.73x","2.19x","6.52x","1.66x","1.38x","2.52x","8.14x"]

# এখানে তোমার সব চ্যানেল লিংক বসাও - ঘুরে ঘুরে আসবে
CHANNELS = [
    "https://t.me/ARYAN_VAI12",
    "https://t.me/ARYAN_VAI12_backup",
    "https://t.me/bdxaryan_official"
]

@bot.message_handler(commands=['start'])
def start(m):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("GET REAL SIGNAL 🚀")
    bot.send_message(m.chat.id, "🔥 ARYAN VIP BIG SIGNAL BOT ONLINE 🟢\n\nGET REAL SIGNAL চাপো 👇", reply_markup=kb)

@bot.message_handler(func=lambda m: m.text and "real signal" in m.text.lower())
def signal(m):
    h = " | ".join(random.sample(HISTORY, 6))
    t = round(random.uniform(2.10, 6.50), 2)
    s1 = round(t * 0.60, 2)
    s2 = round(t - 0.30, 2)
    sid = random.randint(10000, 99999)
    now = datetime.datetime.now().strftime("%I:%M:%S %p")
    
    # Cycling Channel
    channel_link = random.choice(CHANNELS)

    caption = "--------------------------\nAVIATOR VIP BIG SIGNAL\n--------------------------\n\nROUND HISTORY\n" + h + "\n\n--------------------------\nCURRENT FLYING : 2.07x\n--------------------------\n\nMAIN TARGET : " + str(t) + "x\nSAFE 1 : " + str(s1) + "x\nSAFE 2 : " + str(s2) + "x\n\n--------------------------\nID : AV-0424-" + str(sid) + "\nTIME : " + now + "\n--------------------------\n\nSTATUS : PENDING..."

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📢 Channel Join", url=channel_link),
        types.InlineKeyboardButton("🌐 Official Site", url="https://bdxaryan.com")
    )
    markup.add(
        types.InlineKeyboardButton("💬 Support", url="https://t.me/ARYAN_VAI12"),
        types.InlineKeyboardButton("🎁 Bonus Claim", url="https://bdxaryan.com")
    )
    markup.add(
        types.InlineKeyboardButton("▶️ Play Now", url="https://bdxaryan.com")
    )

    bot.send_message(m.chat.id, caption, reply_markup=markup)

print("BOT RUNNING WITH CYCLING CHANNEL")
bot.infinity_polling()
