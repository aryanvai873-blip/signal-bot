import os, random, datetime, io
from PIL import Image, ImageDraw, ImageFont
import telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

CHANNEL_LINK = "https://t.me/sl_communty"
SITE_LINK = "https://bdxaryan35.12bajeevip.com/register.html"
MAIN_USERNAME = "@ARYAN_VAI12"
SECOND_USERNAME = "@TRADER_TAHMID_VAI"

def create_signal_image(multiplier):
    img = Image.new('RGB', (800, 450), color=(15, 15, 15))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0,0),(800,450)], outline=(255,0,0), width=5)
    try:
        font_big = ImageFont.truetype("arial.ttf", 120)
        font_small = ImageFont.truetype("arial.ttf", 35)
    except:
        font_big = ImageFont.load_default()
        font_small = ImageFont.load_default()
    draw.text((250, 30), "AVIATOR", fill=(255,0,0), font=font_small)
    draw.text((200, 120), f"{multiplier}x", fill=(255, 30, 30), font=font_big)
    draw.text((120, 300), f"TAKE PROFIT / CASHOUT: {multiplier}x", fill=(255,255,255), font=font_small)
    bio = io.BytesIO()
    img.save(bio, 'PNG')
    bio.seek(0)
    return bio

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("GET REAL SIGNAL", "ABOUT BOT", "MY ID", "HELP", "BACKUP ID")
    # /start এ লিংক থাকবে
    txt = f"<b>🔥 ARYAN VAI - AVIATOR VIP BOT 🔥</b>\n\nID: 0424 | ONLINE 🟢\n\n<b>🔗 Channel:</b> {CHANNEL_LINK}\n<b>🌐 Site:</b> {SITE_LINK}\n\nনিচ থেকে বাটনে ক্লিক করো 👇"
    bot.send_message(message.chat.id, txt, parse_mode="HTML", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def all_handler(message):
    txt = (message.text or "").lower()
    if "real signal" in txt:
        target = round(random.uniform(1.35, 5.0), 2)
        img_file = create_signal_image(target)
        # সিগন্যালে কোনো লিংক দেই নাই, তাই প্রিভিউ আসবে না
        caption = f"<b>✈️ AVIATOR VIP SIGNAL ✈️</b>\n\n<b>TARGET: {target}x</b>\n<b>SAFE: {round(target-0.3,2)}x</b>\n\n<b>ID: AV-0424-{random.randint(1000,9999)}</b>"
        bot.send_photo(message.chat.id, img_file, caption=caption, parse_mode="HTML")
    elif "about" in txt:
        bot.send_message(message.chat.id, "<b>ABOUT: VIP BOT ID 0424</b>", parse_mode="HTML")
    elif "my id" in txt:
        bot.send_message(message.chat.id, f"ID: <code>{message.from_user.id}</code>", parse_mode="HTML")
    elif "help" in txt:
        bot.send_message(message.chat.id, f"MAIN: {MAIN_USERNAME}", parse_mode="HTML")
    elif "backup" in txt:
        bot.send_message(message.chat.id, f"BACKUP: {SECOND_USERNAME}", parse_mode="HTML")

bot.infinity_polling()
