from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler
from mybot import dispatcher

def eval(update: Update, context: CallbackContext):
    m= update.effective_message
    u = update.effective_user
    
    if u.id != 2142595466:
        m.reply_text(f"Lodu [{u.first_name}](tg://user?id={u.id}) tu mera developer h kya jo eval use kar raha h?",parse_mode=ParseMode.MARKDOWN)
    else:
        text=m.text[len("/eval") :]
        res = text
        m.reply_text("Currently under development")

dispatcher.add_handler(CommandHandler("eval",eval))

        