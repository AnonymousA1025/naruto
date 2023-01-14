import loguru
from pyrogram import Client, filters


api_id = 19500615
api_hash = "7ee1d55d072add75a01e617fc0cef635"
bot_token = "5832903711:AAEc3OWGarirPSDurWqv-xfNc6wun1oXMxU"
app = Client("my_account", 
                        api_id = api_id,
                        api_hash = api_hash,
                        bot_token = bot_token,
                        plugins = {"root":"mybot.modules"}
)

LOGGER = loguru.logger
LOGGER.info("Initialising initial attributes...")