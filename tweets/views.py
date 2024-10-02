from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet


def see_all_tweets(request):
    tweets = Tweet.objects.all()
    print(tweets)
    return render(
        request,
        "all_tweets.html",
        {"tweets": tweets, "title": "Hello! this title comes from django!"},
    )


def see_one_tweet(request, tweet_id):
    return HttpResponse(f"see tweet with id: {tweet_id}")
