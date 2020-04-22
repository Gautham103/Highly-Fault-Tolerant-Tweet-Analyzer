# Highly-Fault-Tolerant-Tweet-Analyzer

A Tweet Analyzer which generates sentiment for a particular tweet topic. This project uses Apache Kafka 2.11-1.1.0 and utilise producer/consumer model where the producer produces stream of real time tweets from the twitter server using tweepy API and the consumer subscribes to the topic which it wants to listen and outputs the sentiment of a tweet topic. 

The above architecture employes three brokers and three zookeeper, thereby making it resilient and fault tolerent. 


## Setup

Update twitter_analyzer_server.py with the credentials
```
consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```
Install the dependent packages
```
pip3 install tweepy textblob
```

Download Apache Kafka 2.11-1.1.0 

Create a file myid and write the id number of zookeeper
```
echo 1 >> sudo vi /tmp/zookeeper1/myid
echo 2 >> sudo vi /tmp/zookeeper2/myid
echo 3 >> sudo vi /tmp/zookeeper3/myid
```

## Steps to Run

1. Start 3 Zookeeper services
```
sudo bin/zookeeper-server-start.sh config/zookeeper1.properties
sudo bin/zookeeper-server-start.sh config/zookeeper2.properties
sudo bin/zookeeper-server-start.sh config/zookeeper3.properties
```
2. Start 3 broker services
```
sudo bin/kafka-server-start.sh config/server1.properties
sudo bin/kafka-server-start.sh config/server2.properties
sudo bin/kafka-server-start.sh config/server3.properties
```
3. Run producer
```
python3 producer.py
```
4. Run Consumer in multiple terminals
```
python3 consumer1.py
python3 consumer2.py
```
