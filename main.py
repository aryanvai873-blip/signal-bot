import os, random, telebot, io
from telebot import types
from PIL import Image, ImageDraw, ImageFont

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

CHANNEL_LINK = "https://t.me/sl_communty"
SITE_LINK = "https://bdxaryan35.12bajeevip.com/register.html"
SUPPORT_LINK = "https://t.me/SIGNAL_MASTERVI1"

def make_img(val):
    W, H = 800, 900
    img = Image.new('RGB', (W, H), (10,10,10))
    d = ImageDraw.Draw(img)
    # বড় হলুদ লেখা
    d.rectangle([(0,0),(W,180)], fill=(20,20,20))
    d.text((W//2,90), "AVIATOR VIP SIGNAL", fill=(255,215,0), anchor="mm", font=ImageFont.load_default())
    # মাঝখানে বড় গুন - এটাই change হবে
    d.text((W//2,400), f"{val}x", fill=(255,255,0), anchor="mm", font=ImageFont.load_default(), align="center")
    # scale করে বড় করো
    img2 = img.resize((800,900))
    # PIL default font ছোট তাই scale trick
    big = Image.new('RGB', (800,900), (10,10,10))
    draw2 = ImageDraw.Draw(big)
    draw2.text((400,90), "VIP SIGNAL", fill=(255,215,0), anchor="mm")
    draw2.text((400,450), f"{val}x", fill=(255,230,0), anchor="mm", stroke_width=2, stroke_fill=(0,0,0))
    # এখানে font size বড় করার জন্য আমরা text কে বড় করে আকছি
    try:
        # যদি arial থাকে
        f1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 140)
        f2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 50)
        big = Image.new('RGB', (800,900), (12,12,16))
        d = ImageDraw.Draw(big)
        d.text((400,120), "VIP SIGNAL", fill=(255,215,0), font=f2, anchor="mm")
        d.text((400,450), f"{val}x", fill=(255,235,100), font=f1, anchor="mm")
        d.text((400,650), "✈️", fill=(255,50,50), font=f1, anchor="mm")
    except:
        pass

    bio = io.BytesIO()
    big.save(bio, 'JPEG')
    bio.seek(0)
    return bio

@bot.message_handler(commands=['start'])
def start(m):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🚀 GET REAL SIGNAL")
    bot.send_message(m.chat.id, "BOT READY", reply_markup=kb)

@bot.message_handler(func=lambda m: "GET REAL SIGNAL" in m.text)
def sig(m):
    main = round(random.uniform(2.5, 20.0), 2)
    s1 = round(main*0.65,2)
    s2 = round(main-0.4,2)
    img = make_img(main)
    cap = f"✈️ VIP SIGNAL\n🎯 MAIN : {main}x\n🛡️ SAFE1 : {s1}x\n🛡️ SAFE2 : {s2}x"
    mk = types.InlineKeyboardMarkup(row_width=2)
    mk.add(types.InlineKeyboardButton("📢 Channel Join", url=CHANNEL_LINK), types.InlineKeyboardButton("🌐 Official Site", url=SITE_LINK))
    mk.add(types.InlineKeyboardButton("💬 Support", url=SUPPORT_LINK), types.InlineKeyboardButton("🎁 Bonus Claim", url=SITE_LINK))
    mk.add(types.InlineKeyboardButton("▶️ Play Now", url=SITE_LINK))
    bot.send_photo(m.chat.id, img, caption=cap, reply_markup=mk)

bot.infinity_polling()
