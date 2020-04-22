import tweepy
import json
import socket
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import kafka
from kafka import KafkaProducer, KafkaClient

consumer_key = 'IBldcrH9B5erhV4sHGqjOX57k'
consumer_secret = 'w2HT6sMuqluRqNPOW6cq2yMSU40anXq2MICuOsuseWFXrFr7yT'
access_token = '1150183553830985728-09CnvReXbvHsIlJLr9R4vojGM4SoSw'
access_token_secret = '9tdNsHUXQdevx5aRtBuFwmtITuC1BmrQajJQY5JN4isK6'

class TweetsListener (StreamListener):
  def __init__ (self):
    super (StreamListener, self).__init__()

  def on_data (self, data):
    try:
      producer.send(kafka_topic, data.encode ('utf-8'))
      msg = json.loads (data)
      print ((msg['text']))
      if ("covid19" in msg['text']):
        producer.send('testTopic', data.encode ('utf-8'))
      if ("trump" in msg['text']):
        producer.send(kafka_topic, data.encode ('utf-8'))

      return True
      exit (0)

    except BaseException as e:
      print ("Error occured")

  def on_error (self, status):
    print (status)
    print ("on_error occured")
    return True




kafka_topic = "sample"
producer = KafkaProducer(bootstrap_servers=['localhost:9092','localhost:9093', 'localhost:9094'])
listener = TweetsListener ()

auth = OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token (access_token, access_token_secret)
twitter_stream = Stream (auth, listener)
twitter_stream.filter (track = ['trump', 'usa', 'covid19'], languages = ['en'])


