from django.db import models

class FeedBackOnDelete(models.Model):
    feed = models.TextField()

    def __str__(self):
        return self.feed
