from django.contrib import admin
from .models import Tweet, Like


class WordFilter(admin.SimpleListFilter):

    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("none", "None"),
            ("Elon Musk", "contained Elon Musk"),
            ("", "not contained Elon Musk"),
        ]

    def queryset(self, request, tweets):
        word = self.value()
        if word:
            return tweets.filter(payload__contains=word)
        else:
            tweets


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "payload",
        "user",
        "created_at",
        "updated_at",
    )
    list_filter = (
        WordFilter,
        "payload",
        "user__username",
        "created_at",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tweet",
        "likes_count",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "user__username",
        "created_at",
    )
