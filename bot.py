import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("TOKEN")

# --- КНОПКИ ---
keyboard = [
    ["😟 Мне тревожно", "😞 Мне грустно"],
    ["😴 Я устал"],
    ["🧘 Дыхательная практика"],
    ["ℹ️ О боте"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)

WELCOME_TEXT = (
    "Привет, бро 💙\n"
    "Я бот психологической поддержки.\n\n"
    "Выбери, что ты сейчас чувствуешь 👇"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "😟 Мне тревожно":
        await update.message.reply_text(
            "Похоже, тебе тревожно 😔\n\n"
            "Попробуй дыхание:\n"
            "— вдох на 4 секунды\n"
            "— пауза 2 секунды\n"
            "— выдох на 6 секунд\n\n"
            "Повтори 5 раз 🫶",
            reply_markup=reply_markup
        )

    elif text == "😞 Мне грустно":
        await update.message.reply_text(
            "Мне жаль, что тебе сейчас грустно 💙\n"
            "Ты не один.\n\n"
            "Иногда помогает просто быть услышанным.\n"
            "Если можешь — поговори с близким человеком.",
            reply_markup=reply_markup
        )

    elif text == "😴 Я устал":
        await update.message.reply_text(
            "Ты правда много на себе несёшь 😔\n\n"
            "Возможно, тебе нужен отдых.\n"
            "Даже короткая пауза — это уже забота о себе.",
            reply_markup=reply_markup
        )

    elif text == "🧘 Дыхательная практика":
        await update.message.reply_text(
            "🧘 Дыхательная практика:\n\n"
            "1️⃣ Вдох через нос — 4 сек\n"
            "2️⃣ Задержка — 2 сек\n"
            "3️⃣ Медленный выдох — 6 сек\n\n"
            "Повтори 5–7 раз.\n"
            "Я здесь, бро 💙",
            reply_markup=reply_markup
        )

    elif text == "ℹ️ О боте":
        await update.message.reply_text(
            "ℹ️ Я учебный бот психологической поддержки.\n\n"
            "Я не врач и не ставлю диагнозы.\n"
            "Если станет очень тяжело — обратись к близким или специалисту.",
            reply_markup=reply_markup
        )

    else:
        await update.message.reply_text(
            "Пожалуйста, выбери вариант из меню 👇",
            reply_markup=reply_markup
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu))

    print("Психолог-бот с меню запущен...")
    app.run_polling()

if __name__ == "__main__":
     main()