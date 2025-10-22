from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# === Sozlamalar ===
TOKEN = "8417560005:AAHqFBzMfL1TsVS0wPfUbuMlSG3xnFP3oNM"
ADMIN_ID = 6885380100  # Sizning Telegram ID'ingiz

# /start buyrug‘i
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "👋 Assalomu alaykum!\n"
        "Bu anonim fikr-mulohaza bot.\n"
        "Yozgan xabaringiz Muhriddingaga anonim tarzda boradi. 💬"
    )

# Oddiy xabarlarni qabul qilish
def handle_message(update: Update, context: CallbackContext):
    msg = update.message.text
    context.bot.send_message(chat_id=ADMIN_ID, text=f"📩 Yangi anonim xabar:\n\n{msg}")
    update.message.reply_text("✅ Xabaringiz anonim tarzda yuborildi. Rahmat!")

# Xatolarni kuzatish
def error(update: Update, context: CallbackContext):
    print(f"Xato yuz berdi: {context.error}")

# Asosiy ishga tushirish
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
