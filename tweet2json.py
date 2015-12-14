'''
Author: Ramiro Aznar
Web: www.ramiroaznar.com
Language: Python
Date: December 14th 2015
Code: print and save as a json file tweets from a certain hashtag, all tweets
are categorized according to their sentiment, question and location if they
have geo tag
Note: to speed up the code, comment "print hashtag_timeline"
'''

#import modules
import oauth2
import json

#declare variables
ckey = "CONSUMER_KEY"
csecret = "CONSUMER_SECRET"
atoken = "ACCESS_TOKEN"
asecret = "ACCESS_SECRET"

#hashtag
hashtag = "hashtag"

#api 
api = "https://api.twitter.com/1.1/search/tweets.json?q=%23" + hashtag + "&src=tyah"


#define oauth request function
def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key, secret)
    token = oauth2.Token(atoken, asecret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content

#print timeline
hashtag_timeline = oauth_req(api, ckey, csecret)
print hashtag_timeline

#save file
saveFile = open('json.csv', 'w')
saveFile.write(hashtag_timeline)
saveFile.close()
