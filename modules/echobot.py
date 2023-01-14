from telegram import Update, ParseMode
from telegram.ext import MessageHandler, CallbackContext, Filters, CommandHandler
from telegram.error import BadRequest
from mybot import dispatcher
from mybot.modules.database.echo_db import insert_value as inv, get_val as gval

def echo_toggle(update: Update, context: CallbackContext):
    m=update.effective_message
    u=update.effective_user
    c=update.effective_chat
    if u.id!=2142595466:
        m.reply_text("You aren't my developer")
    else:
        if m.text[len("/setecho ") :].lower() =="on":
            inv("true")
            m.reply_text("Turned on echo")
        elif m.text[len("/setecho ") :].lower() =="off":
            inv("false")
            m.reply_text("Turned off echo")
        else:
            m.reply_text("Invalid argument")
 

def echo(update: Update, context: CallbackContext) ->str:
    if "true" in gval():
        m = update.effective_message
        chat = update.effective_chat
        bot = context.bot
        xI=bot.copy_message(chat_id=chat.id, from_chat_id=chat.id,message_id=m.message_id,allow_sending_without_reply=True,protect_content=True)
#        xI.reply_copy(from_chat_id=chat.id,allow_sending_without_reply=True)
    else:
        return
        
dispatcher.add_handler(MessageHandler(Filters.all & (~Filters.command), echo))
dispatcher.add_handler(CommandHandler("setecho", echo_toggle))