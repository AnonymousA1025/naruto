from telegram import Update, ParseMode
from telegram.ext import MessageHandler, CallbackContext, CommandHandler, Filters
from mybot import dispatcher, LOGGER

def fwd(update: Update, context: CallbackContext) ->str:
    m=update.effective_message
    c=update.effective_chat
    u=update.effective_user
    bot = context.bot
    x=bot.copy_message(from_chat_id=c.id,chat_id="-1001786686509",message_id=m.message_id)
    LOGGER.info(x)
    m.reply_text("copied")
#    m.reply_copy(chat_id="-1001786686509",reply_to_message_id=False)

dispatcher.add_handler(MessageHandler(Filters.chat_type.private & (~Filters.command), fwd,  run_async=True))
dispatcher.add_handler(CommandHandler("copy",fwd))