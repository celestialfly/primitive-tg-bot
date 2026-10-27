import asyncio
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.constants import ParseMode


TOKEN = "8535731868:AAFEr0bfM69tnLYClK4g4ntLR33mFMbwgGU"
LINK_URL = "https://urlto.me/2EQm4"


keyboard = ReplyKeyboardMarkup(
    [["нажимай"]],
    resize_keyboard=True,
    one_time_keyboard=False
)



# Команда /start – показываем клавиатуру
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Нажми на кнопку ниже 👇",
        reply_markup=keyboard
    )

# Обработка текста (когда нажимают кнопку "Start")
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "нажимай":

        message_text = f'смотри , тут <a href="{LINK_URL}">котик</a>'
        await update.message.reply_text(
            message_text,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True
        )
    else:
        await update.message.reply_text(
            "Пожалуйста, нажми на кнопку «нажимай» в меню.",
            reply_markup=keyboard
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен. Нажми Ctrl+C для остановки.")
    app.run_polling()

if __name__ == "__main__":
    main()