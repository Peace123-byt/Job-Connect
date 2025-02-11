from django.test import TestCase
from rest_framework.test import requests
import json
# from core_root_api.security.user.models import User
class MyAPITests(TestCase):
    # def test_fetch_all_users(self):    
    #     # 2. Use the access token in the Authorization header to fetch all users
    #     users_url = 'http://localhost:8000/user/'
      
    #     response = requests.get(users_url)

    #     # 3. Assert that the request was successful (status code 200)
    #     self.assertEqual(response.status_code, 200)

    #     # 4. (Optional) Add assertions to check the response data
    #     users_data = response.json()
    #     print(users_data)
    #     self.assertIsInstance(users_data, list)  # Check if the response is a list
    
    # def test_register_user_success(self):
    #     # always pass email that is not existing in the database
    #     register_url = 'http://localhost:8000/register/'
    #     register_data = {
    #         'email': 'treasura@example.com',
    #         'full_name': 'Test User',
    #         'student_id': '12345',
    #         'gender': 'Male',
    #         'password': 'securepassword',
    #         'confirm_password': 'securepassword',
    #         'phone_number': '123-456-7890'
    #     }
    #     response = requests.post(register_url, data=register_data)
    #     print(response.json())
    #     self.assertEqual(response.status_code, 201)

    # def test_register_user_exists(self):
        
        # register_url = 'http://localhost:8000/register/'
        # register_data = {
        #     'email': 'treasurep@example.com',
        #     'full_name': 'Test User',
        #     'student_id': '12345',
        #     'gender': 'Male',
        #     'password': 'securepassword',
        #     'confirm_password': 'securepassword',
        #     'phone_number': '123-456-7890'
        # }
        # response = requests.post(register_url, data=register_data)
        # print(response.json())
        # self.assertIn('a', [1,2,3,4])
        # self.assertEqual(response.status_code, 201)

    #     response_data = response.json()
    #     print(response_data)
    #     # self.assertEqual(response_data['status'], False)
    # def test_login_success(self):
  
    #     login_url = 'http://localhost:8000/login/'
    #     login_data = {
    #         'email': 'treasurepeace@gmail.com',
    #         'password': 'Jude1999!'
    #     }
    #     response = requests.post(login_url, data=login_data)

    #     # self.assertEqual(response.status_code, 200)  # Or 200 OK, depending on your API design
    #     response_data = response.json()
    #     print(response_data)
    #     # self.assertEqual(response_data['status'], True)
    #     self.assertEqual(response.status_code, 200)  # Or 200 OK, depending on your API design

        # self.assertIn('access', response_data['data']['access'])  # Assuming access token is returned

    # def test_login_failure(self):
    
    #     login_url = 'http://localhost:8000/login/'
    #     login_data = {
    #         'email': 'treasurepeace@example.com',
    #         'password': 'wrongpassword'
    #     }
    #     response = requests.post(login_url, data=login_data)

    #     self.assertEqual(response.status_code, 401) 
    #     response_data = response.json()
    #     print(response_data)
    #     self.assertEqual(response_data['status'], False)

    def test_string_representation(self):
        post = User(email="user@example.com")
        self.assertEqual(str(post), post.email)
    