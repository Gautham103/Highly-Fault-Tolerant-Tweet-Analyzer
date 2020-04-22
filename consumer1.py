from kafka import KafkaConsumer
import json
import re
from textblob import TextBlob

count = 0
tweets = []

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

consumer = KafkaConsumer('testTopic')
for message in consumer:
    msg = json.loads (message.value)
    if 'text' in msg:
#print (msg['text'])

        parsed_tweet = {}

        parsed_tweet['text'] = msg['text']
#print (get_tweet_sentiment(msg['text']))
        parsed_tweet['sentiment'] = get_tweet_sentiment(msg['text'])

#print (msg['retweet_count'])
        if 1:
            if parsed_tweet not in tweets:
                tweets.append(parsed_tweet)
            else:
                tweets.append(parsed_tweet)

        if count == 10:
            count = 0
            ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
            print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
            ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
            neutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
            print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
            print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
            print("\n\nPositive tweets:")
            for tweet in ptweets[:5]:
                print(tweet['text'])
            print("\n\nNegative tweets:")
            for tweet in ntweets[:5]:
                print(tweet['text'])
            print("\n\nNeutral tweets:")
            for tweet in neutweets[:5]:
                print(tweet['text'])

            tweets = []
        else:
            count = count + 1



consumer.close()

