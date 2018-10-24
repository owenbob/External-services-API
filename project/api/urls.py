"""
Module containing all api app url routes
"""
from django.conf.urls import url
from api.views import SetUp

urlpatterns = [
    url(r'^api/', SetUp.as_view(), name="default")
]

