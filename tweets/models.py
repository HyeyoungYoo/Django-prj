from django.db import models
from common.models import CommonModel


### Tweet model definition ###
class Tweet(CommonModel):
    payload = models.CharField(
        max_length=180,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.payload}"


### Like model definition ###
class Like(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    tweet = models.ForeignKey(
        "Tweet",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user}"
