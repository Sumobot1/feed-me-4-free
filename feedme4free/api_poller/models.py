from __future__ import absolute_import
from django.db import models
import requests
import pytz

from datetime import datetime
from dateutil.tz import tzoffset

# Create your models here.
class TwitterTweetsManager(models.Manager):

    def save_tweet(self, tweet):
        text = tweet.text
        time = tweet.created_at
        url = "https://twitter.com/statuses/{0}".format(tweet.id)
        retweets = tweet.retweet_count
        TwitterTweets.objects.create(text=text, time=time, url=url, retweets=retweets)

class TwitterTweets(models.Model):

    text = models.CharField(max_length=200)
    retweets = models.IntegerField()
    time = models.DateTimeField('date published')
    url = models.CharField(max_length=200)
    objects = TwitterTweetsManager()