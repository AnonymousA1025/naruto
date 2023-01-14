from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler
from mybot import dispatcher 

def typ(update: Update, context: CallbackContext):
    m=update.effective_message
    d=m.reply_to_message.sender_chat
    user=m.reply_to_message.from_user
    
    res=[]
    if d!=None:
        res.append("channel")
    elif user!=None:
        res.append(f"Is bot: {user.is_bot}")
    else:
        res.append(None)
    m.reply_text("I'm alive")
    m.reply_text(res)
    
    
dispatcher.add_handler(CommandHandler ("typ",typ))
