import loguru
import argparse
import logging
import os
from telegram.ext import Updater

LOGGER = loguru.logger
TOKEN = "5832903711:AAEc3OWGarirPSDurWqv-xfNc6wun1oXMxU"
# Python X Gamer's 
#TOKEN = "5684995634:AAHdgAdru91__X_-us_AvEN_fOQlERtpmHQ" 
updater = Updater(token=TOKEN,use_context=True)
dispatcher = updater.dispatcher
LOAD = os.environ.get("LOAD", "").split()
NO_LOAD = os.environ.get("NO_LOAD", "translation").split()

parser = argparse.ArgumentParser()
parser.add_argument(
    '-d', '--debug',
    help="Print lots of debugging statements",
    action="store_const", dest="loglevel", const=logging.DEBUG,
    default=logging.WARNING,
)
parser.add_argument(
    '-v', '--verbose',
    help="Be verbose",
    action="store_const", dest="loglevel", const=logging.INFO,
)
args = parser.parse_args()    
logging.basicConfig(level=args.loglevel)
