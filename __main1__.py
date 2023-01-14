import os
import sys
import importlib
import time
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from mybot import updater, dispatcher, LOGGER
from mybot.modules import ALL_MODULES

IMPORTED = {}
HELPABLE =[]
os.system("clear")
for module_name in ALL_MODULES:
    imported_module = importlib.import_module("mybot.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module


def start(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    msg = """ᴛʜɪs ɪs ᴀɴ ᴜsᴇʟᴇss ʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ'ᴛ ᴅᴏ ᴀɴʏᴛʜɪɴɢ ᴊᴜsᴛ ʜᴀᴠᴇ sᴏᴍᴇ ᴍᴏᴅᴜʟᴇs\n★ ᴏᴡɴᴇʀ sɪʀ :- @PythonXcoder \nsᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ :- @ViolenceChitChat"""
    context.bot.send_message(text=msg,chat_id=chat.id)
    
def exit(update: Update, context: CallbackContext):
    m=update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    text=m.text[len("/exit ") :].lower()
    if chat.type=="supergroup":
        m.reply_text("Pm mai execute kar warna sabko pta chal jayega 🤫")
        return
    else:
        pass
    if user.id !=2142595466:
        m.reply_text("You can't")
        return
    else:
        pass
    if text == "true":
        xd=context.bot.send_message(text="Exiting in 10s",chat_id=chat.id)
        i=10
        while i>=0:
            xd.edit_text(f"Exiting in {i-1}s")
            time.sleep(1)
            i-=1
            if i==0:
                break
        xd.delete()
        m.reply_text("System down")
        sys.exit("Force kill")
        quit()
        sys.exit()
    elif text ==  "false":
        m.reply_text("Then why the hell you execute this command?")
    else:
        m.reply_text("No valid arguments provided")
dispatcher.add_handler(CommandHandler("start",start))
dispatcher.add_handler(CommandHandler("exit",exit))

def main():
    LOGGER.info("Bot is now running!!")

if __name__ == "__main__":
    main()
    updater.start_polling(timeout=15,poll_interval=0,drop_pending_updates=True)
    updater.idle()
    updater.stop()
    os.system("clear")
    LOGGER.info("\033[32m\033[1m"+"Bye")
    input()