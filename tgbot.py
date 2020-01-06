import telegram, sys, random, logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from twitter_scraper import get_tweets

bot_token = sys.argv[1]
twitter_username = sys.argv[2]

tweets = []
for tweet in get_tweets(twitter_username):
	tweets.append(tweet['text'])


bot = telegram.Bot(token=bot_token)

updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="asd")

def tweet(update, context):
	tweet = tweets[random.randint(0, len(tweets))]
	context.bot.send_message(chat_id=update.effective_chat.id, text=tweet)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

tweet_handler = CommandHandler('tweet', tweet)
dispatcher.add_handler(tweet_handler)

updater.start_polling()
