"""
Module containing all api app url routes
"""
from django.conf.urls import url, include
from rest_framework import routers

from api.views import SetUp, ListUsers, RetrieveUser, PostsViewSet, ElasticSearch

router = routers.SimpleRouter()
router.register(r'posts', PostsViewSet, base_name="posts")

urlpatterns = [
    url(r'^$', SetUp.as_view(), name="setup"),
    url(r'^users/', ListUsers.as_view(), name="users"),
    url(r'^search/', ElasticSearch.as_view(),name="search"),
    url(r'^retrieve/(?P<pk>[0-9]+)', RetrieveUser.as_view(), name="retrieve_user"),
    url(r'^', include(router.urls))
]

