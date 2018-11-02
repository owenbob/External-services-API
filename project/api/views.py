from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import requests

from api.serializers import PostsSerializer
from api.models import Posts
from api.search import search

# Create your views here.
USER_BASE_URL = 'https://jsonplaceholder.typicode.com/users'
POSTS_BASE_URL = 'https://jsonplaceholder.typicode.com/posts'

class SetUp(APIView):
    """
    Class to check whether django version 1.11 and 
    django restframework have been properly intergrated.
    """
    def get(self, request):
        message = " You have succesfully setup Django 1.11 and DRF"
        return Response(message)

class ElasticSearch(APIView):
    """
    Class to do a simple search using elastic search
    """
    def get(self, request):
        q = request.query_params.get("q")
        if q:
            response = search(q)
            res = [{"title":b.title,"body":b.body,"id":b.meta.id} for b  in response.hits]
            data = {
                "results":res,
                "results_count":len(res)
            }
            return Response(data)


class ListUsers(APIView):
    """
    Class to list all users from the JsonPlaceHolder  external API
    Reference: 'https://jsonplaceholder.typicode.com/users'
    """
    def get(self, request):
        response = requests.get(USER_BASE_URL)
        if response.status_code == 200:
            return Response(response.json())
        return Response(status=status.HTTP_400_BAD_REQUEST)

class RetrieveUser(APIView):
    """
    class to retrieve specified users from JsonPlaceHolder  external API
    Reference: 'https://jsonplaceholder.typicode.com/users'
    """
    def get(self, request, pk):
        response = requests.get(USER_BASE_URL+"/"+pk)
        if response.status_code == 200:
            return Response(response.json())
        return Response(status=status.HTTP_404_NOT_FOUND)

class PostsViewSet(viewsets.ViewSet):
    """
    Class to handle interaction with post from the JsonPlaceHolder external API
    reference: 'https://jsonplaceholder.typicode.com/users' 
    """

    def list(self, request):
        response = requests.get(POSTS_BASE_URL)
        if response.status_code == 200:
            return Response(response.json())
        return response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        response = requests.get(POSTS_BASE_URL+"/"+pk+"/")
        if response.status_code == 200:
            return Response(response.json())
        return response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):

        title = request.data.get("title")
        body = request.data.get("body")
        
        payload = {
            "title": title,
            "body": body
        }

        post = PostsSerializer(data=payload)

        if post.is_valid():
            post.save()

        response = requests.post(POSTS_BASE_URL,data=payload)
        if response.status_code == 201:
            return Response(response.json(), status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        payload = {
            "title": request.data.get("title"),
            "body": request.data.get("body"),
            "userId": request.data.get("user_id")
        }
        response = requests.put(POSTS_BASE_URL+"/"+pk,data=payload)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        response = requests.put(POSTS_BASE_URL+"/"+pk)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
