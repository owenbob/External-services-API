"""
"""

from api.models import Posts
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Posts)
def index_post(sender, instance, **kwargs):
    instance.indexing()