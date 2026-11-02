import os, random, datetime
import telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

# তোমার সব লিংক
MAIN_USERNAME = "@ARYAN_VAI12"
SECOND_USERNAME = "@TRADER_TAHMID_VAI"
CHANNEL_LINK = "https://t.me/sl_communty"
SITE_LINK = "https://bdxaryan35.12bajeevip.com/register.html"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    # ৫টা বাটন
    markup.add("GET REAL SIGNAL", "ABOUT BOT", "MY ID", "HELP", "BACKUP ID")
    
    txt = f"""
<b>🔥 ARYAN VAI - AVIATOR VIP BOT 🔥</b>

<b>🆔 ID:</b> 0424
<b>Status:</b> ONLINE 🟢
<b>Mode:</b> AVIATOR PREMIUM

<b>🔗 Channel:</b> {CHANNEL_LINK}
<b>🌐 Site:</b> {SITE_LINK}

নিচ থেকে বাটনে ক্লিক করো 👇
"""
    bot.send_message(message.chat.id, txt, parse_mode="HTML", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def all_handler(message):
    text = message.text or ""
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.first_name

    if "REAL SIGNAL" in text:
        # Aviator সিগন্যাল - এটা Practice এর জন্য Random
        target = round(random.uniform(1.30, 3.50), 2)
        safe1 = round(target - 0.3, 2)
        crash_prob = random.choice(["LOW RISK", "MEDIUM RISK", "HIGH RISK"])
        
        msg = f"""
<b>━━━━━━━━━━━━━━━━━━</b>
<b>✈️ AVIATOR VIP SIGNAL ✈️</b>
<b>━━━━━━━━━━━━━━━━━━</b>

<b>🎯 TARGET:</b> {target}x
<b>🛡️ SAFE CASHOUT 1:</b> {safe1}x
<b>⚠️ RISK:</b> {crash_prob}
<b>⏰ TIME:</b> {datetime.datetime.now().strftime('%H:%M:%S')}

<b>🆔 Signal ID:</b> <code>AV-0424-{random.randint(1000,9999)}</code>

<b>💡 Note:</b> Practice Signal - 100% না

<b>━━━━━━━━━━━━━━━━━━</b>
<b>🔗 Channel:</b> {CHANNEL_LINK}
<b>🌐 Site:</b> {SITE_LINK}
<b>━━━━━━━━━━━━━━━━━━</b>
"""
        bot.send_message(chat_id, msg, parse_mode="HTML")

    elif "ABOUT" in text:
        bot.send_message(chat_id, 
            f"<b>🤖 ABOUT BOT</b>\n\n"
            f"<b>Name:</b> ARYAN AVIATOR BOT\n"
            f"<b>ID:</b> 0424\n"
            f"<b>Version:</b> VIP Premium\n"
            f"<b>Channel:</b> {CHANNEL_LINK}\n"
            f"<b>Site:</b> {SITE_LINK}",
            parse_mode="HTML")

    elif "MY ID" in text:
        bot.send_message(chat_id, 
            f"<b>🆔 YOUR INFO</b>\n\n"
            f"<b>Name:</b> {name}\n"
            f"<b>User ID:</b> <code>{user_id}</code>\n"
            f"<b>Bot:</b> @YourBot\n"
            f"<b>Channel:</b> {CHANNEL_LINK}",
            parse_mode="HTML")

    elif "HELP" in text:
        bot.send_message(chat_id, 
            f"<b>🆘 MAIN SUPPORT</b>\n\n"
            f"<b>📩 Main ID:</b> {MAIN_USERNAME}\n"
            f"<b>🔗 Channel:</b> {CHANNEL_LINK}\n"
            f"<b>🌐 Site:</b> {SITE_LINK}\n\n"
            f"যেকোনো সমস্যায় Main ID তে মেসেজ দাও",
            parse_mode="HTML")

    elif "BACKUP" in text:
        bot.send_message(chat_id, 
            f"<b>🔐 BACKUP SUPPORT</b>\n\n"
            f"<b>📩 Backup ID:</b> {SECOND_USERNAME}\n"
            f"<b>🔗 Channel:</b> {CHANNEL_LINK}\n"
            f"<b>🌐 Site:</b> {SITE_LINK}\n\n"
            f"Main ID না পেলে Backup এ মেসেজ দাও",
            parse_mode="HTML")

print("BOT RUNNING - AVIATOR WITH 5 BUTTONS")
bot.infinity_polling()
