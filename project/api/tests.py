"""
Module to handle tests for external services
"""
from unittest.mock import patch, Mock, MagicMock
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory


from api.views import (
    ListUsers,
    RetrieveUser,
    PostsViewSet
    )
from  api.mock_functions import (
    list_users_side_effect,
    retrieve_user_side_effect,
    list_posts_side_effect,
    retrieve_post_side_effect,
    create_post_side_effect,
    update_post_side_effect,
    destroy_post_side_effect

)


class TestExternalServicesTestCase(APITestCase):
    """
    class to test external service routes
    """
    def setUp(self):
        self.factory = APIRequestFactory()
        
    @patch("api.views.ListUsers.get",side_effect=list_users_side_effect)
    def test_list_users(self,mock_list_users):
                
        request = self.factory.get('/api/users/')
        resp = ListUsers.as_view()(request)
        self.assertEquals(resp.status_code,200) 
        self.assertEquals(resp.data[0]["id"],1)
        self.assertEquals(resp.data[0]["name"],"Leanne Graham")
        self.assertEquals(resp.data[0]["username"],"Bret")
        self.assertEquals(resp.data[0]["phone"],"1-770-736-8031 x56442")

    @patch("api.views.RetrieveUser.get",side_effect=retrieve_user_side_effect)
    def test_retrieve_user(self,mock_retrieve_user):

        request = self.factory.get('/api/retrieve/2')
        resp = RetrieveUser.as_view()(request)
        self.assertEquals(resp.status_code,200) 
        self.assertEquals(resp.data["id"],2)
        self.assertEquals(resp.data["name"],"Ervin Howell")
        self.assertEquals(resp.data["username"],"Antonette")
        self.assertEquals(resp.data["phone"],"010-692-6593 x09125")

    @patch("api.views.PostsViewSet.list",side_effect=list_posts_side_effect)
    def test_list_posts(self,mock_list_posts):
        request = self.factory.get('/api/posts/')
        resp = PostsViewSet.as_view(actions ={'get': 'list'})(request)
        self.assertEquals(resp.status_code,200)
        self.assertEquals(len(resp.data),2) 
        self.assertEquals(resp.data[0]["id"],1)
        self.assertEquals(resp.data[1]["id"],2)

    @patch("api.views.PostsViewSet.retrieve",side_effect=retrieve_post_side_effect)
    def test_retrieve_post(self,mock_retrieve_post):

        request = self.factory.get('/api/posts/2')
        resp = PostsViewSet.as_view(actions ={'get': 'retrieve'})(request)
        self.assertEquals(resp.status_code,200)
        self.assertEquals(resp.data["id"],2)
        self.assertEquals(resp.data["title"],"qui est esse")
        self.assertEquals(resp.data["body"],"est rerum tempore vitae")


    @patch("api.views.PostsViewSet.create",side_effect=create_post_side_effect)
    def test_create_post(self, mock_create_post):
        test_payload = {
        "title": "Test_title",
        "body": "test_body",
        "userId": "1"
        }
        request = self.factory.post('/api/posts/',test_payload)
        resp = PostsViewSet.as_view(actions ={'post': 'create'})(request)
        self.assertEquals(resp.status_code,201)
        self.assertNotEquals(resp.data["title"], "Test Body")
        self.assertNotEquals(resp.data["body"], "Test Body")
        
    @patch("api.views.PostsViewSet.update",side_effect=update_post_side_effect)
    def test_update_post(self, mock_update_post):
        test_payload = {
        "userId":"1",
        "title": "Test Update title",
        "body": "Test Update body"
        }
        request = self.factory.put('/api/posts/',test_payload)
        resp = PostsViewSet.as_view(actions ={'put': 'update'})(request)
        self.assertEquals(resp.status_code,200)
        self.assertEquals(resp.data["title"], "Test Update title")
        self.assertEquals(resp.data["body"], "Test Update body")

    @patch("api.views.PostsViewSet.destroy",side_effect=destroy_post_side_effect)
    def test_destroy_post(self, mock_destroy_post):

        request = self.factory.delete('/api/posts/3')
        resp = PostsViewSet.as_view(actions ={'delete': 'destroy'})(request)
        self.assertEquals(resp.status_code,200)
        self.assertEquals(resp.data["title"], "Test delete title")
        self.assertEquals(resp.data["body"], "Test delete body")

#Using  Testing Context Manager 

