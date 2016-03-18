#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, requests, random
from auth_flickr import *

JPG_NAME = 'phallus.jpg'

def get_image(text):
    res = requests.get('https://api.flickr.com/services/rest/', params = {
        'method': 'flickr.photos.search',
        'api_key': API_KEY,
        'text': text,
        'sort': 'relevance',
        'per_page': 500,
        'page': random.randint(1, 3),
        'format': 'json',
        'nojsoncallback': 1
    })

    p = res.json()['photos']['photo'][random.randint(1, 500)]
    url = "https://farm%s.staticflickr.com/%s/%s_%s.jpg" % (p['farm'], p['server'], p['id'], p['secret'])
    image = request_search(url)
    f = open(JPG_NAME, 'wb')
    f.write(image.content)
    f.close()
    return JPG_NAME

def request_search(url):
    while True:
        image = requests.get(url)
        if image.status_code == 200:
            return image
