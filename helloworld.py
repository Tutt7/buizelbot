# !usr/bin/env python
# -*- coding: utf- 8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

CONSUMER_KEY = 'lreEDtVJf9FHfPrah7MtMrm1J'
CONSUMER_SECRET = 'u3fcTPqFEjh4ZLdOr1rpyNkuiRItnywzjioU2IiVnGDNuTEDWj'
ACCESS_KEY = '1078653829934182400-bFw5oLEULD20h0btvYUiOE5W0ZnB9F'
ACCESS_SECRET = 'rYKWllYbw4QERLjpdYAICw1RhNi87ZHgpxjrWRfAn3PZ8'

auth = tweepy.OauthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()
for line in f:
    api.update_status(line)
    time.sleep(900)
