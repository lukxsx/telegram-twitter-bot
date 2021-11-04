import telegram, sys, random
from telegram.ext import Updater, CommandHandler
from twitter_scraper import get_tweets


def tweet(update, context):
	tweet = tweets[random.randint(0, len(tweets))]
	#fix parsing error that breaks image tweet links
	if "pic" in tweet:
		tweet = tweet.split("pic.twitter.com")
		tweet = tweet[0] + " pic.twitter.com" + tweet[1]

	context.bot.send_message(chat_id=update.effective_chat.id, text=tweet)
	print(tweet)


def main(argv):
	bot_token = sys.argv[1]
	twitter_username = sys.argv[2]
	
	tweets = []
	for tweet in get_tweets(twitter_username):
		tweets.append(tweet['text'])

	bot = telegram.Bot(token=bot_token)
	updater = Updater(token=bot_token, use_context=True)
	dispatcher = updater.dispatcher
	
	tweet_handler = CommandHandler('tweet', tweet)
	dispatcher.add_handler(tweet_handler)
	updater.start_polling()


if __name__ == "__main__":
	print(len(sys.argv))
	if len(sys.argv) != 3:
		print('How to use: python %s <bot token> <twitter username>' % sys.argv[0])
	else:
		main(sys.argv)
