from __future__ import absolute_import
from django.conf import settings

from api_poller.models import TwitterTweets
from feedme4free.celery import app

from celery.task.schedules import crontab
from celery.task import periodic_task
import tweepy
from datetime import timedelta

auth_twitter = tweepy.OAuthHandler(settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET)
auth_twitter.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)

api_twitter = tweepy.API(auth_twitter)

@app.periodic_task(run_every=timedelta(seconds=30), name='api_poller.tasks.get_twitter_tweets')
def get_twitter_tweets():
    for tweet in tweepy.Cursor(api_twitter.search,
                               q="%23freefood",
                               count=10,
                               result_type="recent",
                               include_entities=True,
                               lang="en").items():
        TwitterTweets.objects.save_tweet(tweet)