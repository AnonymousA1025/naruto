from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler
from mybot import dispatcher, LOGGER
from typing import Optional
from mybot.modules.admin_chk import admin_check


def ban(update: Update, context: CallbackContext) -> Optional[str]:
    bot = context.bot
    m = update.effective_message
    chat = update.effective_chat
    user = m.reply_to_message.from_user
    channel = m.reply_to_message.sender_chat
    try:
            bot.ban_chat_sender_chat(sender_chat_id=channel.id, chat_id=chat.id)
            
    except Exception as e:
            LOGGER.debug(e)
            bot.send_message(text=e, chat_id=chat.id)
    else:
            bot.send_message(text=f"Successfully banned: [{channel.title}](t.me/{channel.username})",chat_id=chat.id, parse_mode=ParseMode.MARKDOWN,disable_web_page_preview=True)
 
def unban(update: Update, context: CallbackContext):
    m=update.effective_message
    channel=m.reply_to_message.sender_chat
    bot = context.bot
    chat= update.effective_chat
    dn=bot.unban_chat_sender_chat(sender_chat_id=channel.id, chat_id=chat.id)
    if dn:
        m.reply_text(f"Successfully unbanned: [{channel.title}](t.me/{channel.username})", parse_mode=ParseMode.MARKDOWN,disable_web_page_preview=True)
    else:
        m.reply_text("Damn I can't ban that user")
        

dispatcher.add_handler(CommandHandler ("cban", ban))
dispatcher.add_handler(CommandHandler("cunban",unban))

    
    