from rest_framework import serializers

from api.models import Posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ("id", "title", "body")