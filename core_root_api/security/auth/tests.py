# from django.test import TestCase

# # Create your tests here.
# import pytest
# from django.urls import reverse
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options  # Or FirefoxOptions
# from core_root_api.security.user.models import User # Import User model


# class SeleniumTests(StaticLiveServerTestCase):
#     # port = 8000  # Change this if you need to run on a different port
#     host = 'localhost'  # Change this if you need to run on a different host
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()

#         # Set Chrome options (headless mode)
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")  # Run in headless mode (no browser window)
#         chrome_options.add_argument("--no-sandbox")  # Required for running in Docker/CI
#         chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crashes in headless Chrome
#         # Set the path to your ChromeDriver executable
#         cls.selenium = webdriver.Chrome(options=chrome_options) # Or Firefox()
#         cls.selenium.implicitly_wait(10)  # Wait up to 10 seconds for elements to load

#         # Create a test user
#         cls.test_user = User.objects.create_user(email='testuser', password='testpassword')

#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super().tearDownClass()

#     def test_landing_page(self):
#         self.selenium.get(f'{self.live_server_url}{reverse("index")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("index")}')

#     def test_about_us_page(self):
#         self.selenium.get(f'{self.live_server_url}{reverse("aboutus")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("aboutus")}')

#     def test_contact_us_page(self):
#         self.selenium.get(f'{self.live_server_url}{reverse("contactus")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("contactus")}')

#     def test_admin_login_page(self):
#         self.selenium.get(f'{self.live_server_url}{reverse("adminlogin")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("adminlogin")}')

#     def test_job_list_post_page(self):
#         self.selenium.get(f'{self.live_server_url}{reverse("joblistpost")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("joblistpost")}')

#     def test_admin_signup_page(self):
#         self.selenium.get(f'{self.live_server_url}{reverse("adminsignup")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("adminsignup")}')

#     def test_admin_profile_page(self):
#         # Login
#         self.selenium.get(f'{self.live_server_url}{reverse("adminlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your password field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector

#         # Verify successful login (you might need a better check here)
#         # Check if it redirects to the profile page
#         self.selenium.get(f'{self.live_server_url}{reverse("adminprofile")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("adminprofile")}')

#     def test_student_login_page(self):
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("studentlogin")}')

#     def test_apply_job_page(self):
#         # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your password field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector

#         self.selenium.get(f'{self.live_server_url}{reverse("apply-job", args=["1"])}')  # Replace 1 with a valid job ID
#         # You'll need to create a Job object with ID 1 in your test database
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("apply-job", args=["1"])}')

#     def test_student_signup_page(self):
#         self.selenium.get(f'{self.live_server_url}{reverse("studentsignup")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("studentsignup")}')

#     def test_logout_page(self):
#         # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your password field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector

#         self.selenium.get(f'{self.live_server_url}{reverse("logout")}')
#         # After logout, it should redirect to the landing page or login page
#         # Check the redirection target
#         self.assertIn(f'{self.live_server_url}', self.selenium.current_url)  # Expect redirect to the landing page or login

#     def test_reset_password_page(self):
#         self.selenium.get(f'{self.live_server_url}{reverse("resetpassword")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("resetpassword")}')

#     def test_change_password_page(self):
#           # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your password field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector

#         self.selenium.get(f'{self.live_server_url}{reverse("change-password")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("change-password")}')

#     def test_student_profile_page(self):
#         # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your password field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector

#         self.selenium.get(f'{self.live_server_url}{reverse("studentprofile")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("studentprofile")}')

#     def test_company_profile_page(self):
#         # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your password field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector
#         self.selenium.get(f'{self.live_server_url}{reverse("companyprofile")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("companyprofile")}')

#     def test_applied_job_page(self):
#         # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your password field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector
#         self.selenium.get(f'{self.live_server_url}{reverse("appliedjob", args=["1"])}')  # Replace 1 with a valid job ID
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("appliedjob", args=["1"])}')

#     def test_single_job_page(self):
#         self.selenium.get(f'{self.live_server_url}{reverse("singlejob", args=["1"])}')  # Replace 1 with a valid job ID/PK
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("singlejob", args=["1"])}')

#     def test_student_dashboard_page(self):
#         # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your password field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector
#         self.selenium.get(f'{self.live_server_url}{reverse("studentdashboard")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("studentdashboard")}')

#     def test_detailed_saved_job_page(self):
#          # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your username field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector
#         self.selenium.get(f'{self.live_server_url}{reverse("detailedsavedjob", args=["1"])}')  # Replace 1 with a valid job ID
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("detailedsavedjob", args=["1"])}')

#     def test_successful_submission_page(self):
#          # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your password field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector
#         self.selenium.get(f'{self.live_server_url}{reverse("submit-application", args=["1"])}')  # Replace 1 with a valid job ID
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("submit-application", args=["1"])}')

#     def test_withdraw_application_page(self):
#          # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your password field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector
#         self.selenium.get(f'{self.live_server_url}{reverse("withdrawapplication", args=["1"])}')  # Replace 1 with a valid job ID
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("withdrawapplication", args=["1"])}')

#     def test_company_dashboard_page(self):
#          # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your password field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector
#         self.selenium.get(f'{self.live_server_url}{reverse("companydashboard")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("companydashboard")}')

#     def test_post_job_page(self):
#          # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your password field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector
#         self.selenium.get(f'{self.live_server_url}{reverse("postjob")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("postjob")}')

#     def test_edit_job_page(self):
#          # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your username field
#         username_input.send_keys("testuser")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector
#         self.selenium.get(f'{self.live_server_url}{reverse("edit-job", args=[1])}')  # Replace 1 with a valid job ID
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("edit-job", args=[1])}')

#     def test_job_applications_page(self):
#          # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your username field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector
#         self.selenium.get(f'{self.live_server_url}{reverse("jobapplications")}')
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("jobapplications")}')

#     def test_download_cv_page(self):
#         # Login (similar to admin_profile_page)
#         self.selenium.get(f'{self.live_server_url}{reverse("studentlogin")}')
#         username_input = self.selenium.find_element("id","id_username") # Replace with the actual id of your username field
#         password_input = self.selenium.find_element("id","id_password") # Replace with the actual id of your password field
#         username_input.send_keys("testuser")
#         password_input.send_keys("testpassword")
#         self.selenium.find_element("xpath", "//button[@type='submit']").click() # Replace with your submit button selector
#         self.selenium.get(f'{self.live_server_url}{reverse("download_cv", args=["test_cv.pdf"])}')  # Replace 'test_cv.pdf' with a valid filename
#         self.assertEqual(self.selenium.current_url, f'{self.live_server_url}{reverse("download_cv", args=["test_cv.pdf"])}')

