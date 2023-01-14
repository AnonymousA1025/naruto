from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler
from mybot import dispatcher, LOGGER

def rep(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    replied = message.reply_to_message.from_user
    message.reply_text(f"{replied.id}")

def gay(update: Update, context: CallbackContext):
    m = update.effective_message
    replied = m.reply_to_message.from_user
    user = update.effective_user
    if replied.id !=2142595466:
        text = f"[{replied.first_name}](tg://user?id={replied.id}) is a gay 😂"
    else:
        text = f"[{user.first_name}](tg://user?id={user.id}) is a gay 😂"
    m.reply_to_message.reply_text(text, parse_mode=ParseMode.MARKDOWN)

dispatcher.add_handler(CommandHandler("rid",rep))
dispatcher.add_handler(CommandHandler("gay",gay))