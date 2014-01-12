#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
import secret

class twitterapi:
    def __init__(self):
        self.api = twitter.Api( 
            consumer_key        = secret.dict['CONSUMER_KEY'],
            consumer_secret     = secret.dict['CONSUMER_SECRET'],
            access_token_key    = secret.dict['ACCESS_TOKEN'],
            access_token_secret = secret.dict['ACCESS_TOKEN_SECRET']
        )
        self.terms = secret.terms

    def verifyCredentials(self):
        return self.api.VerifyCredentials()

    def getUserTimelineFromAccount(self, name='wkodate', cnt=20):
        statuses = self.api.GetUserTimeline(screen_name=name, count=cnt)
        for s in statuses:
            print s.text.encode('utf-8')

    def getTweetsWithLoco(self, name='wkodate', cnt=20):
        statuses = self.api.GetUserTimeline(screen_name=name, count=cnt)
        for s in statuses:
            if (s.place is None):
                continue
            print '[text]'+s.text.encode('utf-8')
            print '[place]'+s.place['full_name'].encode('utf-8')
            coordinates = s.place['bounding_box']['coordinates'][0]
            for i in range(len(coordinates)):
                print "[boundingBox%d] %f, %f" \
                        % (i, coordinates[i][0], coordinates[i][1])

    def searchTweetsFromTerm(self, tm, cnt=200):
        statuses = self.api.GetSearch(term=tm, count=cnt)
        for s in statuses:
            if (s.place is None):
                continue
            print s.text.encode('utf-8')
            print s

    def searchTweetsFromList(self, cnt=200):
        for tm in self.terms:
            statuses = self.api.GetSearch(term=tm, count=cnt)
            if (statuses is None) :
                continue
            for s in statuses:
                if (s.place is None):
                    continue
                print s.text.encode('utf-8')
                print s.place['full_name'].encode('utf-8')
                print s                
