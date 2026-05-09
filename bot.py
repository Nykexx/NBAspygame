import os
import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)

BOT_TOKEN = "8383248985:AAFaukYmGc-kLjCSNJU4K7L5n1ykdQxwJ-U"
WEB_APP_URL = "https://astounding-sunflower-bb9e50.netlify.app/"# https://your-username.github.io/nba-spy


async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏀 *NBA SPY*\n\nНайди шпиона среди игроков НБА!\n\n"
        "208 игроков · 5 уровней сложности · Current & All\\-Time",
        parse_mode="MarkdownV2",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("🕵️ Играть", web_app=WebAppInfo(url=WEB_APP_URL))
        ]])
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", app_start := start))
    logging.info("Bot running. Web App: %s", WEB_APP_URL)
    app.run_polling()


if __name__ == "__main__":
    main()
