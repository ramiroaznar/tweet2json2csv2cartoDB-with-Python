# Tweets to json to csv to CartoDB with Python.

These three Python scripts (*tweet2json.py*, *json2csv.py* and *csv2cartodb.py*) allows you to import tweets from a certain hashtag, first to a json file, then to a csv file and finally to CartoDB in order to visualize them.

## tweet2json.py

This program prints and imports to a json file the time line from a certain API request related to a certain hastag. 

## json2csv.py

This program imports to a csv file the time, user, text, sentiment, question, place, latitude and longitude of all 
the tweets from a json file. 

## csv2cartodb.py

This program imports from a csv file the twitter information to a CartoDB dataset. It also contains
the instructions to generate a animated point data map using Torque.

### Requisites:

First, it is necessary to get your CartoDB API from the following link:

- CartoDB: http://docs.cartodb.com/cartodb-platform/sql-api/authentication/

In addition, in order to run these programs you must download and install the following modules:

- Tweepy: https://github.com/tweepy/tweepy
- Geopy: https://github.com/geopy/geopy
- TextBlob: https://github.com/sloria/TextBlob
- CartoDB: https://github.com/CartoDB/cartodb-python

### Final thoughts:

I recommend to use *timeline2csv.py* or *tweet2csv.py* from the [twitter2cartodb-with-python repository](https://github.com/ramiroaznar/twitter2cartodb-with-Python) instead of *tweet2json.py* and *json2csv.py*
because the formers are faster and one-step scripts.

