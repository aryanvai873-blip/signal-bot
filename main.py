import os, random, telebot, io
from telebot import types
from PIL import Image, ImageDraw, ImageFont

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

CH = "https://t.me/sl_communty"
SITE = "https://bdxaryan35.12bajeevip.com/register.html"
SUP = "https://t.me/SIGNAL_MASTERVI1"

def make_img(val):
    W=800; H=900
    im=Image.new('RGB',(W,H),(12,12,16))
    d=ImageDraw.Draw(im)
    try:
        f1=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",140)
        f2=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",45)
    except:
        f1=ImageFont.load_default(); f2=f1
    d.text((W//2,120),"VIP SIGNAL",fill=(255,215,0),font=f2,anchor="mm")
    d.text((W//2,450),f"{val}x",fill=(255,235,100),font=f1,anchor="mm",stroke_width=3,stroke_fill=(0,0,0))
    d.text((W//2,650),"AVIATOR",fill=(200,200,200),font=f2,anchor="mm")
    bio=io.BytesIO()
    im.save(bio,'JPEG')
    bio.seek(0)
    return bio

@bot.message_handler(commands=['start'])
def start(m):
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🚀 GET REAL SIGNAL")
    bot.send_message(m.chat.id,"🔥 VIP BOT ONLINE",reply_markup=kb)

@bot.message_handler(func=lambda m: "GET REAL SIGNAL" in m.text)
def sig(m):
    main=round(random.uniform(3.5,18.0),2)
    s1=round(main*0.65,2)
    s2=round(main-0.4,2)
    img=make_img(main)
    cap=f"✈️ VIP SIGNAL\n🎯 MAIN : {main}x\n🛡️ SAFE1 : {s1}x\n🛡️ SAFE2 : {s2}x\n\n⏳ PENDING..."
    mk=types.InlineKeyboardMarkup(row_width=2)
    mk.add(types.InlineKeyboardButton("📢 Channel Join",url=CH),types.InlineKeyboardButton("🌐 Official Site",url=SITE))
    mk.add(types.InlineKeyboardButton("💬 Support",url=SUP),types.InlineKeyboardButton("🎁 Bonus Claim",url=SITE))
    mk.add(types.InlineKeyboardButton("▶️ Play Now",url=SITE))
    bot.send_photo(m.chat.id,img,caption=cap,reply_markup=mk)

bot.infinity_polling()
