from telegram import Update
from telegram.ext import CommandHandler
from telegram.ext import ApplicationBuilder, MessageHandler, CallbackContext
from telegram.ext import filters
from lib.chat import ai_reply


async def response(update: Update, context: CallbackContext):
    response = ai_reply(update.message.text)
    await update.message.reply_text(response)

async def initializeChat( update: Update, context: CallbackContext) :
    await update.message.reply_text("Hey there! Delighted to have you here. Feel free to ask anything ")

if __name__ == '__main__' :
    app = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()
    app.add_handler(CommandHandler('start', initializeChat))
    app.add_handler(MessageHandler(filters.TEXT, response))
    app.run_polling()