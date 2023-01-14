from telegram import Update, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler
from mybot import dispatcher, LOGGER

def id(update: Update, context: CallbackContext) -> str:
    m = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    text = f"ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ ɪs: {user.id}`\nᴄʜᴀᴛ ɪᴅ ɪs :-  {chat.id}"
    try:
        m.reply_text(text)
    except Exception as e:
        m.reply_text(e)

def info(update: Update, context: CallbackContext):
    m = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    image = "https://telegra.ph/file/95be0987f75aac235f14a.jpg"
    try:
        profile = context.bot.get_user_profile_photos(user.id).photos[0][-1]
        context.bot.sendChatAction(chat.id, "upload_photo")
    except Exception as e:
         profile=image

    text = f"""Your Info: 
       ★ **ғɪʀsᴛ ɴᴀᴍᴇ** :- {user.first_name}
       ★ **ʟᴀsᴛ ɴᴀᴍᴇ** :- {user.last_name}
       ★ **ᴜsᴇʀ ɪᴅ** :- {user.id}
       ★ **ᴘʀᴏғɪʟᴇ ʟɪɴᴋ** :- [{user.first_name}](tg://user?id={user.id})
       ★ **ᴜsᴇʀɴᴀᴍᴇ** :- @{user.username}"""
    markup1 = [
    [
    InlineKeyboardButton("Profile",url=f"https://t.me/{user.username}"),
    ],
    [
    InlineKeyboardButton("Support",url="https://t.me/ViolenceChitChat")
    ],
    ]
    reply_markup=InlineKeyboardMarkup(markup1)
    try: 
        m.reply_photo(photo=profile, caption=text,reply_markup=reply_markup,parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        LOGGER.debug(e)
        context.bot.send_message(text=f"{e}", chat_id=chat.id, parse_mode=ParseMode.MARKDOWN)
    
dispatcher.add_handler(CommandHandler("id",id))
dispatcher.add_handler(CommandHandler("info",info))