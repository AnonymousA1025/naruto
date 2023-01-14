from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler
from mybot import dispatcher 

def leave(update: Update, context: CallbackContext):
    _ = update
    m = _.effective_message
    c = _.effective_chat
    u = _.effective_user
    bot = context.bot
    if u.id !=2142595466:
        m.reply_text("You're not my developer")
    else:
        bot.leave_chat(c.id)

dispatcher.add_handler(CommandHandler ("lv",leave))