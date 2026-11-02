from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# --- এখানে তোমার ইনফো বসানো আছে ---
BOT_TOKEN = "এখানে তোমার BotFather এর Token বসাও"
SITE_LINK = "https://bdxaryan35.12bajeevip.com/register.html"
CHANNEL_LINK = "https://t.me/sl_communty"
CHANNEL_USERNAME = "@sl_communty"

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("📡 ARYAN VAI SIGNAL", callback_data='signal')],
        [InlineKeyboardButton("🎮 AVIATOR GAME LINK", url=SITE_LINK)],
        [InlineKeyboardButton("💰 DEPOSIT / WITHDRAW", callback_data='deposit')],
        [InlineKeyboardButton("📊 TODAY RESULT", callback_data='result')],
        [InlineKeyboardButton("📞 SUPPORT", url=CHANNEL_LINK)]
    ]
    return InlineKeyboardMarkup(keyboard)

def join_keyboard():
    keyboard = [
        [InlineKeyboardButton("1️⃣ Channel Join করো", url=CHANNEL_LINK)],
        [InlineKeyboardButton("2️⃣ Site এ Register করো", url=SITE_LINK)],
        [InlineKeyboardButton("🔄 Check করে Bot Start করো ✅", callback_data='check_join')]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 আসসালামু আলাইকুম!\n\nARYAN VAI BOT চালু করতে নিচের ২ টা কাজ করো:\n\n1. আমাদের Channel @sl_communty তে Join করো\n2. সাইটে Register করো\n\nতারপর Check বাটনে ক্লিক করো 👇",
        reply_markup=join_keyboard()
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'check_join':
        try:
            member = await context.bot.get_chat_member(CHANNEL_USERNAME, query.from_user.id)
            if member.status in ['member', 'administrator', 'creator']:
                await query.edit_message_text(
                    "✅ ভেরিফাইড! Welcome to ARYAN VAI BOT 👇\n\nনিচ থেকে অপশন সিলেক্ট করো:",
                    reply_markup=main_menu_keyboard()
                )
            else:
                await query.answer("❌ ভাই আগে চ্যানেলে Join করো, তারপর Check দাও!", show_alert=True)
        except Exception as e:
            print(e)
            await query.answer("❌ Bot টিকে চ্যানেলের Admin বানাও নাই। আগে Admin বানাও!", show_alert=True)

    elif query.data == 'signal':
        await query.edit_message_text("📡 Signal আসছে... এইখানে তুমি তোমার Signal লেখা বসাতে পারবে।", reply_markup=main_menu_keyboard())
    elif query.data == 'deposit':
        await query.edit_message_text(f"💰 Deposit করতে এই লিংকে যাও:\n{SITE_LINK}", reply_markup=main_menu_keyboard())
    elif query.data == 'result':
        await query.edit_message_text("📊 আজকের রেজাল্ট: Win ✅", reply_markup=main_menu_keyboard())

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("Bot is running... @sl_communty Bot")
app.run_polling()
