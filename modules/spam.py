from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from mybot import dispatcher, LOGGER

def spam(update: Update, context: CallbackContext) -> None:
    m = update.effective_message
    text = m.text[len("/spam ") :]
    chat = update.effective_chat
    bot = context.bot
    try:
        rn = int(text[0: 1])
        LOGGER.info(rn)
    except Exception as e:
        rn = int(text[0])
        LOGGER.info(rn)
        
    for x in range(rn):
        bot.send_message(text=text, chat_id=chat.id)

dispatcher.add_handler(CommandHandler("spam", spam))
