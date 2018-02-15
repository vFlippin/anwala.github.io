import json
import pandas as pd
import matplotlib.pyplot as plt
import re


tweets_data_path = 'lateset.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print (len(tweets_data))

# tweets = pd.DataFrame()

# tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)

def extract_link(text):
    regex = r'(?P<url>https?://[^\s]+)' #r'(?:(https?|s?ftp):\/\/)?' + r'(?:www\.)?' #r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

# tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

# tweets_with_link = tweets['link'] != ''

# print (tweets_with_link['link'])

with open('testrun2.txt', 'r') as f:
    for line in f:
        try:
            tweet = json.loads(line)
            link = extract_link(tweet['text'])
            if link != '':
                print (link)
        except:
            continue
