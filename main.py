import os, random, telebot
from telebot import types
from PIL import Image, ImageDraw, ImageFont
import io

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

CHANNEL_LINK = "https://t.me/sl_communty"
SITE_LINK = "https://bdxaryan35.12bajeevip.com/register.html"
SUPPORT_LINK = "https://t.me/SIGNAL_MASTERVI1"

def create_vip_image(multiplier_text):
    # 800x1000 কালো ব্যাকগ্রাউন্ড
    W, H = 800, 1000
    img = Image.new('RGB', (W, H), color=(8, 8, 12))
    draw = ImageDraw.Draw(img)
    
    try:
        # Render এ font না থাকলে default use হবে
        font_big = ImageFont.truetype("arial.ttf", 180)
        font_mid = ImageFont.truetype("arial.ttf", 55)
        font_small = ImageFont.truetype("arial.ttf", 40)
    except:
        font_big = ImageFont.load_default()
        font_mid = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # VIP SIGNAL
    draw.text((W//2, 150), "VIP SIGNAL", fill=(255,215,0), font=font_mid, anchor="mm")
    # লাইন
    draw.text((W//2, 220), "— AVIATOR • SIGNAL • MULTIPLIER —", fill=(180,180,180), font=font_small, anchor="mm")
    
    # বড় গুন - যেটা change হবে
    draw.text((W//2, 420), f"{multiplier_text}x", fill=(255, 225, 80), font=font_big, anchor="mm", stroke_width=4, stroke_fill=(80,50,0))
    
    # প্লেনের effect - লাল লাইন
    draw.ellipse((150, 600, 650, 850), fill=(30, 10, 10), outline=(255, 50, 50), width=5)
    draw.text((W//2, 730), "✈️", fill=(255,80,80), font=ImageFont.truetype("arial.ttf", 150) if 'arial.ttf' in os.listdir('.') else font_big, anchor="mm")

    # নিচে ছোট লেখা
    draw.text((W//2, 950), "ARYAN VAI • VIP", fill=(100,100,100), font=font_small, anchor="mm")

    # bytes এ convert
    bio = io.BytesIO()
    bio.name = 'vip.jpg'
    img.save(bio, 'JPEG', quality=95)
    bio.seek(0)
    return bio

@bot.message_handler(commands=['start'])
def start(msg):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🚀 GET REAL SIGNAL")
    bot.send_message(msg.chat.id, "🔥 VIP BOT ONLINE 🟢", reply_markup=kb)

@bot.message_handler(func=lambda m: "GET REAL SIGNAL" in m.text)
def signal(msg):
    main = round(random.uniform(2.50, 15.00), 2)
    safe1 = round(main * 0.65, 2)
    safe2 = round(main - 0.40, 2)
    
    # এই main টাই ছবিতে যাবে
    photo_file = create_vip_image(f"{main}")

    caption = f"✈️ VIP SIGNAL\n\n🎯 MAIN : {main}x\n🛡️ SAFE 1 : {safe1}x\n🛡️ SAFE 2 : {safe2}x\n\n⏳ STATUS : PENDING..."

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📢 Channel Join", url=CHANNEL_LINK),
        types.InlineKeyboardButton("🌐 Official Site", url=SITE_LINK)
    )
    markup.add(
        types.InlineKeyboardButton("💬 Support", url=SUPPORT_LINK),
        types.InlineKeyboardButton("🎁 Bonus Claim", url=SITE_LINK)
    )
    markup.add(types.InlineKeyboardButton("▶️ Play Now", url=SITE_LINK))

    bot.send_photo(msg.chat.id, photo=photo_file, caption=caption, reply_markup=markup)

print("BOT RUNNING - DYNAMIC IMAGE MODE")
bot.infinity_polling()
