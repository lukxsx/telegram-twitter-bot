import telegram
import sys
from telegram.ext import Updater
bot_token = sys.argv[1]

bot = telegram.Bot(token=bot_token)
