@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("1️⃣ Channel Join করো", url="https://t.me/sl_communty"),
        types.InlineKeyboardButton("2️⃣ Site এ Register করো", url="https://bdxaryan35.12bajeevip.com/register.html"),
        types.InlineKeyboardButton("🔄 Check করে Bot Start করো ✅", callback_data="check_join")
    )
    bot.send_message(message.chat.id, "🔥 ARYAN VAI VIP BOT চালু করতে ২টা কাজ করো:\n\n1. Channel @sl_communty তে Join করো\n2. Site এ Register করো\n\nতারপর Check বাটনে ক্লিক করো 👇", reply_markup=markup)
