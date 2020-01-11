import telegram, sys, random
from telegram.ext import Updater, CommandHandler
from twitter_scraper import get_tweets

bot_token = sys.argv[1]
twitter_username = sys.argv[2]

tweets = []
for tweet in get_tweets(twitter_username):
	tweets.append(tweet['text'])

bot = telegram.Bot(token=bot_token)

updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

def tweet(update, context):
	tweet = tweets[random.randint(0, len(tweets))]
	if "pic" in tweet:
		tweet = tweet.split("pic.twitter.com")
		tweet = tweet[0] + " pic.twitter.com" + tweet[1]

	context.bot.send_message(chat_id=update.effective_chat.id, text=tweet)
	print(tweet)

tweet_handler = CommandHandler('tweet', tweet)
dispatcher.add_handler(tweet_handler)

updater.start_polling()
