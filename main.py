import os
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("✅ Signal Bot Live! 24h Running")

async def signal(update, context):
    await update.message.reply_text("📈 BUY Signal: BTC/USDT\nEntry: 65000\nTP: 67000\nSL: 64000")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))
print("Bot starting...")
app.run_polling()
