from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# === Sozlamalar ===
TOKEN = "8417560005:AAHqFBzMfL1TsVS0wPfUbuMlSG3xnFP3oNM"
ADMIN_ID = 6885380100  # Sizning Telegram ID'ingiz

# /start buyrug‘i
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Assalomu alaykum!\n"
        "Bu anonim fikr-mulohaza bot.\n"
        "Yozgan habaringiz Muhriddinga anonim tarzda boradi. 💬"
    )

# Oddiy xabarlarni saqlash
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    with open('messages.txt', 'a', encoding='utf-8') as f:
        f.write(msg + "\n---\n")
    await update.message.reply_text("✅ Xabaringiz anonim tarzda yuborildi!")

# Admin uchun /all — barcha xabarlarni ko‘rish
async def show_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id != ADMIN_ID:
        await update.message.reply_text("🚫 Sizda bu buyrug‘ni ishlatish huquqi yo‘q.")
        return

    try:
        with open('messages.txt', 'r', encoding='utf-8') as f:
            content = f.read().strip()
        if not content:
            await update.message.reply_text("📭 Hozircha anonim xabarlar yo‘q.")
        else:
            await update.message.reply_text(f"📬 Anonim xabarlar:\n\n{content}")
    except FileNotFoundError:
        await update.message.reply_text("📭 Hozircha anonim xabarlar yo‘q.")

# /clear — barcha xabarlarni o‘chiradi
async def clear_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id != ADMIN_ID:
        await update.message.reply_text("🚫 Sizda bu buyrug‘ni ishlatish huquqi yo‘q.")
        return

    open('messages.txt', 'w').close()
    await update.message.reply_text("🗑️ Barcha anonim xabarlar o‘chirildi.")

# === Botni ishga tushirish ===
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("all", show_all))
app.add_handler(CommandHandler("clear", clear_messages))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🤖 Bot ishga tushdi...")
app.run_polling()

