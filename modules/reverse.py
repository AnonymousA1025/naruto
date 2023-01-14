from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler 
from mybot import dispatcher 


def reverse(update: Update, context: CallbackContext):
    m=update.effective_message
    text = m.text[len("/treverse ") :]
    if text:
        m.reply_text(text[::-1])
    else:
        m.reply_text("Noobde kuch text toh de")

dispatcher.add_handler(CommandHandler("treverse", reverse))