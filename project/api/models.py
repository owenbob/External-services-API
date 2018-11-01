from django.db import models
from django.conf import settings


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)

    def __str__(self):
        return("{}".format(self.title))

    # Add indexing method to Posts
    def indexing(self):
        obj = PostsIndex(
            meta={'id': self.id},
            title=self.title,
            body=self.body
        )
        obj.save()
        return obj.to_dict(include_meta=True)

from api.search import PostsIndex