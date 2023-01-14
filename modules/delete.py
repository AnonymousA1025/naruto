import time
from telegram import Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler

from mybot import dispatcher, LOGGER

def delete(update: Update, context: CallbackContext) -> None:
    m = update.effective_message
    bot = context.bot
    replied = m.reply_to_message
    if replied:
        replied.delete()
        m.delete()
    else:
        m.reply_text("Reply to a message to delete it")
 

def purge(update: Update, context: CallbackContext) -> None:
    m = update.effective_message
    chat = update.effective_chat
    bot = context.bot
    msg = m.reply_to_message
    t1 = time.time()
    if not msg:
        m.reply_text("Reply to a message to select where to start purging from.")
        return
    i = 10
    if i == 10:
        msg_id = msg.message_id
        count = 0
        to_delete = m.message_id - 1
        todel1 = m.message_id
        m.delete()
        msg.delete()

        for m_id in range(todel1, msg_id +1):
            try:
                bot.delete_message(message_id=m_id, chat_id=chat.id)
            except BadRequest as e:
                LOGGER.debug(e)

        for m_id in range(to_delete, msg_id - 1, -1):
            try:
                bot.delete_message(chat_id=chat.id,message_id=m_id)
                count+=1
            except BadRequest:
                pass

        bot.send_message(text=f"deleted {count} messages in {time.time() - t1:.3f}s", chat_id = chat.id)
 
dispatcher.add_handler(CommandHandler("del", delete))
dispatcher.add_handler(CommandHandler("purge",purge))