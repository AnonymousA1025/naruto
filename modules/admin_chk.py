from telegram import Update
from telegram.ext import CallbackContext

def admin_check(update: Update, context: CallbackContext):
    chat = update.effective_chat
    bot = context.bot
    user = update.effective_user
    status=bot.get_chat_member(chat.id, user.id).status
    if status:
        if status in {"creator","administrator"}:
            return True
        else:
            return False