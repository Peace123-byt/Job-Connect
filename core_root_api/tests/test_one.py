import pytest
# from core.fixtures.user import user
# from core.post.models import Post
from core_root_api.security.user.models import User
data_user = {
    "email":"kezechristian@gmail.com",
 "full_name": "eze kc",
 "student_id": "12345678",
 "gender": "Male",
 "password": "Password1999!",
 "confirm_password": "Password1999!",
 "phone_number":"+2348082182438"
}
def add(x,y):
    return x+y
def test_sum():
 assert add(1, 2) == 3

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(**data_user)
    assert user.email == data_user["email"]
    assert user.phone_number == data_user["phone_number"]
    assert user.full_name == data_user["full_name"]
    assert user.student_id == data_user["student_id"]



# @pytest.fixture
# def post(db, user):
#     return Post.objects.create(author=user,
#     body="Test Post Body")

# import pytest


# # Testing the REST API 106
# @pytest.mark.django_db
# def test_create_comment(user, post):
#     comment = Comment.objects.create(
#         author=user,
#         post=post,
#         body="Test Comment Body"
#     )
    
#     assert comment.author == user
#     assert comment.post == post
#     assert comment.body == "Test Comment Body"


# import pytest
# from rest_framework.test import APIClient
# @pytest.fixture
# def client():
#     return APIClient()
  
# import pytest
# from rest_framework import status

# class TestAuthenticationViewSet:
#     endpoint = 'localhost:8000/'

#     def test_login(self, client):
#         data = {
#         "email": "kc@gmail.com",
#         "password": "test_password"
#         }
#         response = client.post(self.endpoint + "login/",
#         data)
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['access']
    
#         assert response.data['user']['email'] == user.email

#     @pytest.mark.django_db
#     def test_register(self, client):
#         data = {
#     "email":"kezechris@gmail.com",
#  "full_name": "eze k",
#  "student_id": "12345678",
#  "gender": "Male",
#  "password": "Password1999!",
#  "confirm_password": "Password1999!",
#  "phone_number":"+2348082182438"
# }
#         response = client.post(self.endpoint + "register/",
#         data)
#         # assert response.status_code ==status.HTTP_201_CREATED

#     def test_refresh(self, client, user):
#         data = {
#         "username": user.username,
#         "password": "test_password"
#         }
#         response = client.post(self.endpoint + "login/",
#         data)
#         assert response.status_code == status.HTTP_200_OK
#         data_refresh = {
#         "refresh": response.data['refresh']
#         }
#         response = client.post(self.endpoint + "refresh/",
#         data_refresh)
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['access']