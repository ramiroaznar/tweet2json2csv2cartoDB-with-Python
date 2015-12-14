'''
Author: Ramiro Aznar
Web: www.ramiroaznar.com
Language: Python
Date: December 14th 2015
Code: convert json to csv file, extracting tweet by tweet
time, user, text, sentiment analysis, question, place,
longitude and latitude
'''

#import module
import json

from csv import writer

import geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim()

from textblob import TextBlob

from datetime import datetime

#input file
with open('json.csv') as data_file:
	data = json.load(data_file)

tweets = data['statuses']

#variables
times = [tweet['created_at'] for tweet in tweets]
print times
users = [tweet['user']['name'] for tweet in tweets]
texts = [tweet['text'] for tweet in tweets]
#sentiment analysis
feelings = [TextBlob(tweet['text']) for tweet in tweets]
sentiments = []
for f in feelings:
        if f.sentiment.polarity > 0:
                sentiments.append("positive")
        else:
                if f.sentiment.polarity < 0:
                        sentiments.append("negative")
                else:
                        sentiments.append("neutral")

#question
questions = ["yes" if "?" in tweet['text'] else "no" for tweet in tweets]
#coordinates
places = [(T['place']['full_name'] if T['place'] else geolocator.reverse(str(T['geo']['coordinates'])) if T['geo'] else None) for T in tweets]
lats = [(T['geo']['coordinates'][0] if T['geo'] else geolocator.geocode(T['place']['full_name']).latitude if T['place'] else None) for T in tweets]
lons = [(T['geo']['coordinates'][1] if T['geo'] else geolocator.geocode(T['place']['full_name']).longitude if T['place'] else None) for T in tweets]

#output file
out = open('tweets_hashtag.csv', 'w')
print >> out, 'Time,User,Text,Sentiment,Question,Place,Latitude,Longitude'

rows = zip(times, users, texts, sentiments, questions, places, lats, lons)

csv = writer(out)

for row in rows:
    values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
    csv.writerow(values)

out.close()

