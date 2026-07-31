import os 
from downloader import download_video
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Assalomu alaykum!\n\n"
        "Menga Instagram, YouTube, TikTok yoki Facebook video havolasini yuboring.\n"
        "Men sizga videoni va MP3 musiqasini yuboraman."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Qo'llab-quvvatlanadi:\n"
        "• Instagram\n"
        "• TikTok\n"
        "• YouTube\n"
        "• Facebook"
    )

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    msg = await update.message.reply_text("⏳ Video yuklanmoqda...")

    try:
        video = download_video(url)

        await update.message.reply_video(video=open(video, "rb"))

        os.remove(video)

        await msg.edit_text("✅ Tayyor!")

    except Exception as e:
        await msg.edit_text(f"❌ Xatolik:\n{e}")
    await update.message.reply_text(
        "⏳ Havola qabul qilindi.\nVideo yuklanmoqda..."
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
