# 8749485122:AAH215z4qH5t-rO21yBZJngeMA3fZRintA4
import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext
from telegram.helpers import effective_message_type

TOKEN = "8749485122:AAH215z4qH5t-rO21yBZJngeMA3fZRintA4"
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE ):
    await update.message.reply_text(f"Hello, {update.effective_user.first_name}!")

async def text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Hello, {update.effective_user.first_name}! You said: {text}!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text))
app.run_polling()




