import os, random, telebot, io
from telebot import types
from PIL import Image, ImageDraw, ImageFont

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

CH = "https://t.me/sl_communty"
SITE = "https://bdxaryan35.12bajeevip.com/register.html"
SUP = "https://t.me/SIGNAL_MASTERVI1"

def make_dynamic(val):
    # তোমার base.jpg টা খুলবে
    try:
        im = Image.open("base.jpg").convert("RGB")
    except:
        # যদি base.jpg না থাকে তাহলে কালো বানাবে
        im = Image.new('RGB', (800, 900), (12,12,16))
    W,H = im.size
    d = ImageDraw.Draw(im)
    # মাঝখানের পুরানো 5.22x টা কালো দিয়ে ঢেকে দাও
    d.rectangle([(0, int(H*0.15)), (W, int(H*0.48))], fill=(8,8,15))
    
    try:
        f1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(W*0.23))
        f2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(W*0.055))
    except:
        f1 = ImageFont.load_default()
        f2 = f1

    d.text((W//2, int(H*0.10)), "VIP SIGNAL", fill=(255,215,0), font=f2, anchor="mm")
    # নতুন গুন - এটাই Dynamic
    d.text((W//2, int(H*0.31)), f"{val}x", fill=(255,230,80), font=f1, anchor="mm", stroke_width=4, stroke_fill=(80,60,0))
    d.text((W//2, int(H*0.44)), "AVIATOR • SIGNAL • MULTIPLIER", fill=(180,160,90), font=f2, anchor="mm")

    bio = io.BytesIO()
    im.save(bio, 'JPEG', quality=95)
    bio.seek(0)
    return bio

@bot.message_handler(commands=['start'])
def start(m):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🚀 GET REAL SIGNAL")
    bot.send_message(m.chat.id, "🔥 VIP READY", reply_markup=kb)

@bot.message_handler(func=lambda m: "GET REAL SIGNAL" in m.text)
def sig(m):
    main = round(random.uniform(4.5, 19.0), 2)
    s1 = round(main*0.65, 2)
    s2 = round(main-0.4, 2)
    img = make_dynamic(main)
    cap = f"✈️ VIP SIGNAL\n🎯 MAIN : {main}x\n🛡️ SAFE1 : {s1}x\n🛡️ SAFE2 : {s2}x\n\n⏳ PENDING..."
    mk = types.InlineKeyboardMarkup(row_width=2)
    mk.add(types.InlineKeyboardButton("📢 Channel Join", url=CH), types.InlineKeyboardButton("🌐 Official Site", url=SITE))
    mk.add(types.InlineKeyboardButton("💬 Support", url=SUP), types.InlineKeyboardButton("🎁 Bonus Claim", url=SITE))
    mk.add(types.InlineKeyboardButton("▶️ Play Now", url=SITE))
    bot.send_photo(m.chat.id, img, caption=cap, reply_markup=mk)

bot.infinity_polling()
