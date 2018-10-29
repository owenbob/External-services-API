"""
Module conatining mock fucntion that should act as side effect 
functions for testing our view functions using Mock.side_effect
"""

from rest_framework.response import Response
from rest_framework import status


def list_users_side_effect(list):
    expected_list = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    }]
    
    return Response(expected_list)

def retrieve_user_side_effect(user):
    user = {
                "id": 2,
                "name": "Ervin Howell",
                "username": "Antonette",
                "email": "Shanna@melissa.tv",
                "address": {
                    "street": "Victor Plains",
                    "suite": "Suite 879",
                    "city": "Wisokyburgh",
                    "zipcode": "90566-7771",
                    "geo": {
                        "lat": "-43.9509",
                        "lng": "-34.4618"
                    }
                },
                "phone": "010-692-6593 x09125",
                "website": "anastasia.net",
                "company": {
                    "name": "Deckow-Crist",
                    "catchPhrase": "Proactive didactic contingency",
                    "bs": "synergize scalable supply-chains"
                }
            }

    return Response(user)
    
def list_posts_side_effect(posts):
    expected_posts = [
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat ",
        "body": "quia et suscipit"
    },
    {
        "userId": 1,
        "id": 2,
        "title": "qui est esse",
        "body": "est rerum tempore vitae"
    }
    ]
    return Response(expected_posts)

def retrieve_post_side_effect(post):
    post = {
        "userId": 1,
        "id": 2,
        "title": "qui est esse",
        "body": "est rerum tempore vitae"
    }
    return Response(post)

def create_post_side_effect(post):
    create_post = {
        "userId": 1,
        "id": 2,
        "title": "Test title",
        "body": "Test body"
    }
    return Response(create_post,status=status.HTTP_201_CREATED)

def update_post_side_effect(post):
    update_post = {
        "userId": 1,
        "id": 2,
        "title": "Test Update title",
        "body": "Test Update body"
    }
    return Response(update_post)


def destroy_post_side_effect(post):
    destroy_post = {
        "userId": 1,
        "id": 3,
        "title": "Test delete title",
        "body": "Test delete body"
    }
    return Response(destroy_post)

