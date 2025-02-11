# # from django.test import LiveServerTestCase
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # import time

# # class NavigationTest(LiveServerTestCase):
# #     def setUp(self):
# #         # Initialize the Chrome webdriver.
# #         self.selenium = webdriver.Chrome()  # Specify executable_path if needed.
# #         self.selenium.implicitly_wait(10)  # Wait up to 10 seconds for elements to load.
# #         super().setUp()

# #     def tearDown(self):
# #         # Quit the webdriver after each test.
# #         self.selenium.quit()
# #         super().tearDown()

# #     def test_navigation_through_pages(self):
# #         """
# #         This test will navigate through a series of pages, pausing 2 seconds between each.
# #         Modify the URL patterns and any dynamic segments (e.g., job_id) as needed.
# #         """
# #         # List of page paths to visit (update dynamic parts as needed)
# #         paths = [
# #             '/',  # Landing page (index)
# #             '/about-us',
# #             '/contact-us',
# #             '/admin-login',
# #             '/job-list',
# #             '/admin-signup',
# #             '/admin-profile',
# #             '/student-login',
# #             '/apply-job/1',         # Replace '1' with a valid job id in your test database.
# #             '/student-signup',
# #             '/logout',
# #             '/reset-password',
# #             '/change-password',
# #             '/student-profile',
# #             '/company-profile',
# #             '/job/applied/1',       # Replace '1' with a valid job id.
# #             '/single-job/1',        # Replace '1' with a valid primary key.
# #             '/student-dashboard',
# #             '/student/job/saved/1', # Replace '1' with a valid job id.
# #             '/successful-submission/1', # Replace '1' with a valid job id.
# #             '/withdraw-application/1',  # Replace '1' with a valid job id.
# #             '/company-dashboard',
# #             '/job/create/',
# #             '/job/edit/1/',         # Replace '1' with a valid job id.
# #             '/job/applications/',
# #             '/download-cv/test_cv.pdf/'  # Replace 'test_cv.pdf' with an existing filename.
# #         ]

# #         # Loop through each path and visit the page.
# #         for path in paths:
# #             url = f'{self.live_server_url}{path}'
# #             self.selenium.get(url)
# #             print(f"Visited: {url}")
# #             time.sleep(2)  # Pause for 2 seconds before moving to the next page.

# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# class NavigationTest(StaticLiveServerTestCase):
#     port = 8000  # Force the test server to run on port 8000

#     def setUp(self):
#         # Initialize the Chrome webdriver.
#         self.selenium = webdriver.Chrome()  # Specify executable_path if needed.
#         self.selenium.implicitly_wait(10)  # Wait up to 10 seconds for elements to load.
#         super().setUp()

#     def tearDown(self):
#         # Quit the webdriver after each test.
#         self.selenium.quit()
#         super().tearDown()

#     def test_navigation_through_pages(self):
#         """
#         This test will navigate through a series of pages, pausing 2 seconds between each.
#         Static files (including images) will now be served automatically.
#         """
#         # List of page paths to visit (update dynamic segments as needed)
#         paths = [
#             '/',  # Landing page (index)
#             '/about-us',
#             '/contact-us',
#             '/admin-login',
#             '/job-list',
#             '/admin-signup',
#             '/admin-profile',
#             '/student-login',
#             '/apply-job/1',         # Replace '1' with a valid job id in your test database.
#             '/student-signup',
#             '/logout',
#             '/reset-password',
#             '/change-password',
#             '/student-profile',
#             '/company-profile',
#             '/job/applied/1',       # Replace '1' with a valid job id.
#             '/single-job/1',        # Replace '1' with a valid primary key.
#             '/student-dashboard',
#             '/student/job/saved/1', # Replace '1' with a valid job id.
#             '/successful-submission/1', # Replace '1' with a valid job id.
#             '/withdraw-application/1',  # Replace '1' with a valid job id.
#             '/company-dashboard',
#             '/job/create/',
#             '/job/edit/1/',         # Replace '1' with a valid job id.
#             '/job/applications/',
#             '/download-cv/test_cv.pdf/'  # Replace 'test_cv.pdf' with an existing filename.
#         ]

#         # Loop through each path and visit the page.
#         for path in paths:
#             url = f'{self.live_server_url}{path}'
#             self.selenium.get(url)
#             print(f"Visited: {url}")
#             time.sleep(2)  # Pause for 2 seconds before moving to the next page.





# import pytest
# from django.urls import reverse
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from core_root_api.security.user.models import User  # Import User model
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# class SeleniumTests(StaticLiveServerTestCase):
#     port = 8000
#     host = 'localhost'

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()

#         chrome_options = Options()
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")

#         cls.selenium = webdriver.Chrome(options=chrome_options)
#         cls.selenium.implicitly_wait(10)

#         # Create a test user (for login)
#         cls.test_user = User.objects.create_user(email='ezekc@gmail.com', password='testpassword')

#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super().tearDownClass()


#     def test_student_login_form(self):
#         """Tests student login form submission."""
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')

#         # 1. Find the elements (replace with your actual IDs/selectors)
#         username_field = self.selenium.find_element("id", "id_username")  # ***REPLACE***
#         password_field = self.selenium.find_element("id", "id_password")  # ***REPLACE***
#         submit_button = self.selenium.find_element("xpath", "//button[@type='submit']")  # ***REPLACE***

#         # 2. Enter the values
#         username_field.send_keys("testuser")
#         password_field.send_keys("testpassword")

#         # 3. Submit the form
#         submit_button.click()

#         # 4. Assert success (VERY IMPORTANT!)
#         # Example: Check for a redirect to the student dashboard
#         WebDriverWait(self.selenium, 10).until(
#             EC.url_contains(reverse("studentdashboard"))  # Wait for redirect
#         )
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("studentdashboard")}')

#         # Example: Check for a welcome message
#         # welcome_message = self.selenium.find_element("id", "welcome-message").text # ***REPLACE***
#         # self.assertIn("Welcome, testuser!", welcome_message)

#     def test_student_signup_form(self):
#         """Tests student signup form submission."""
#         self.selenium.get(f'{self.live_server_url}{reverse("studentsignup")}')

#         # 1. Find the elements (replace with your actual IDs/selectors)
#         email_field = self.selenium.find_element("id", "email")  # ***REPLACE***
#         # ***REPLACE***
#         password_field = self.selenium.find_element("id", "password")  # ***REPLACE***  (Assuming password confirmation)
#         confirm_password_field = self.selenium.find_element("id", "confirm_password")  # ***REPLACE***
#         submit_button = self.selenium.find_element("xpath", "//button[@type='submit']")  # ***REPLACE***
#         # 2. Enter the values (replace with your test data)
#         email_field.send_keys("test@example.com")
#         password_field.send_keys("testpassword")
#         confirm_password_field.send_keys("testpassword")
#         # 3. Submit the form
#         submit_button.click()
#         # 4. Assert success (VERY IMPORTANT!)
#         # Example: Check for a redirect (e.g., to the login page or profile page)
#         WebDriverWait(self.selenium, 10).until(
#             EC.url_contains(reverse("studentlogin"))  # Wait for redirect
#         )
#         # Example: Check if user is created and redirects to login
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("studentlogin")}')


# import pytest
# from core.user.models import User
# data_user = {
#  "email": "test_user",
#  "email": "test@gmail.com",
#  "first_name": "Test",
#  "last_name": "User",
#  "password": "test_password"
# }