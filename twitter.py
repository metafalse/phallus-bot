#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, flickr
from auth_twitter import *
from requests_oauthlib import OAuth1Session

session = OAuth1Session(CK, CS, AT, AS)

def tweet(status):
    validate_res(session.post('https://api.twitter.com/1.1/statuses/update.json', params = {"status": status}))

def tweet_image(status, image):
    res_media = session.post('https://upload.twitter.com/1.1/media/upload.json', files = {'media': open(image, 'rb')})
    validate_res(res_media)
    validate_res(session.post('https://api.twitter.com/1.1/statuses/update.json', params = {"status": status, 'media_ids': res_media.json()['media_id']}))

def delete(id):
    validate_res(session.post("https://api.twitter.com/1.1/statuses/destroy/%d.json" % id))

def print_user_timeline(screen_name):
    res = session.get('https://api.twitter.com/1.1/statuses/user_timeline.json', params = {"screen_name": screen_name})
    validate_res(res)
    for status in res.json():
        print status[u'text']

def get_friends(screen_name):
    res = session.get('https://api.twitter.com/1.1/friends/list.json', params = {"screen_name": screen_name})
    validate_res(res)
    for user in res.json()['users']:
        print user['screen_name']
        print user['name']

def follow(screen_name):
    validate_res(session.post('https://api.twitter.com/1.1/friendships/create.json', params = {"screen_name": screen_name}))

def validate_res(res):
    print 'OK' if res.status_code == 200 else "Error: %d" % res.status_code

if sys.argv[1] == 'tweet':
    tweet(sys.argv[2])
elif sys.argv[1] == 'tweet_image':
    tweet_image(sys.argv[2], sys.argv[3])
elif sys.argv[1] == 'tweet_phallus':
    flickr.get_image('phallus')
    tweet_image('Phallus', 'phallus.jpg')
elif sys.argv[1] == 'delete':
    delete(sys.argv[2])
elif sys.argv[1] == 'print_user_timeline':
    print_user_timeline(sys.argv[2])
elif sys.argv[1] == 'get_friends':
    get_friends(sys.argv[2])
elif sys.argv[1] == 'follow':
    follow(sys.argv[2])
