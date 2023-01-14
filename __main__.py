import asyncio
from pyrogram import idle, filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from . import LOGGER, app
START_BUTTONS  = [[InlineKeyboardButton("JOIN HERE", url = "t.me/TeamXScenario"), InlineKeyboardButton("MY DEV", url = "http://t.me/Lime_user_01")]]
@app.on_message(filters.command('start'))
async def command1(bot, message):
		await message.reply_photo (photo = "https://te.legra.ph/file/2304724bad5e7108d7c25.jpg", caption = "•Welcome to my personal assistant bot\n•I haven't added much features yet but there are many features upcoming soon\n•My master is @Lime_user_01 :)",
	reply_markup = InlineKeyboardMarkup(START_BUTTONS))	


@app.on_message(filters.command('help'))
async def command2(bot, m):
    await m.reply("This is the help section of test bot :)\n•/id - Use this command to get your and the chat's id\n•/start - Use this to start the bot\n•/help - See all commands and explaination.")
@app.on_message(filters.command('rebutt'))
async def restart():
	app.stop()
	app.start()
	idle()
	await message.reply_text("restarting...")

async def main():
    try:
        LOGGER.info("Starting bot...")
        await app.start()
    except Exception as e:
        LOGGER.debug(e)
    else:
        await app.send_message(5963610296, "On hogya Bhai 🌝")
        LOGGER.info("Bot started...")
        await idle()
        LOGGER.info("Stopping bot...")
        await app.stop()

app.run(main())