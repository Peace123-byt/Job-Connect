# from django.test import TestCase

# # Create your tests here.
# from django.test import TestCase, Client
# from django.urls import reverse
# from core_root_api.security.user.models import User  # For testing authenticated views

# class IntegrationTests(TestCase):
#     def setUp(self):
#         # Create a test client
#         self.client = Client()

#         # Optionally, create a test user for authenticated views
#         self.test_user = User.objects.create_user(
#             email='testuser', password='testpassword'
#         )

#     def test_landing_page(self):
#         """Tests the landing page URL."""
#         response = self.client.get(reverse('index'))  # Use the name from urls.py
#         self.assertEqual(response.status_code, 200)

#     def test_about_us_page(self):
#         """Tests the about us page URL."""
#         response = self.client.get(reverse('aboutus'))
#         self.assertEqual(response.status_code, 200)

#     def test_contact_us_page(self):
#         """Tests the contact us page URL."""
#         response = self.client.get(reverse('contactus'))
#         self.assertEqual(response.status_code, 200)

#     def test_admin_login_page(self):
#         """Tests the admin login page URL."""
#         response = self.client.get(reverse('adminlogin'))
#         self.assertEqual(response.status_code, 200)  # Or 302 if redirecting

#     def test_job_list_post_page(self):
#         """Tests the job list page URL."""
#         response = self.client.get(reverse('joblistpost'))
#         self.assertEqual(response.status_code, 200)

#     def test_admin_signup_page(self):
#         """Tests the admin signup page URL."""
#         response = self.client.get(reverse('adminsignup'))
#         self.assertEqual(response.status_code, 200)

#     def test_admin_profile_page(self):
#         """Tests the admin profile page URL (requires login)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('adminprofile'))
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()

#     def test_student_login_page(self):
#         """Tests the student login page URL."""
#         response = self.client.get(reverse('studentlogin'))
#         self.assertEqual(response.status_code, 200)

#     def test_apply_job_page(self):
#         """Tests the apply job page URL (requires login and a job_id)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('apply-job', args=['test_job_id']))  # Replace 'test_job_id' with a valid job ID
#         self.assertEqual(response.status_code, 200)  # Or 302 if redirecting
#         self.client.logout()

#     def test_student_signup_page(self):
#         """Tests the student signup page URL."""
#         response = self.client.get(reverse('studentsignup'))
#         self.assertEqual(response.status_code, 200)

#     def test_logout_page(self):
#         """Tests the logout page URL (requires login)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('logout'))
#         self.assertEqual(response.status_code, 302)  # Expect a redirect after logout
#         self.client.logout()

#     def test_reset_password_page(self):
#         """Tests the reset password page URL."""
#         response = self.client.get(reverse('resetpassword'))
#         self.assertEqual(response.status_code, 200)

#     def test_change_password_page(self):
#         """Tests the change password page URL (requires login)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('changepassword'))
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()

#     def test_student_profile_page(self):
#         """Tests the student profile page URL (requires login)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('studentprofile'))
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()

#     def test_company_profile_page(self):
#         """Tests the company profile page URL (requires login)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('companyprofile'))
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()

#     def test_applied_job_page(self):
#         """Tests the applied job page URL (requires login and a job_id)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('appliedjob', args=['test_job_id']))  # Replace 'test_job_id' with a valid job ID
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()

#     def test_single_job_page(self):
#         """Tests the single job page URL (requires a primary_key)."""
#         response = self.client.get(reverse('singlejob', args=['test_primary_key']))  # Replace 'test_primary_key' with a valid primary key
#         self.assertEqual(response.status_code, 200)

#     def test_student_dashboard_page(self):
#         """Tests the student dashboard page URL (requires login)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('studentdashboard'))
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()

#     def test_detailed_saved_job_page(self):
#         """Tests the detailed saved job page URL (requires login and a job_id)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('detailedsavedjob', args=['test_job_id']))  # Replace 'test_job_id' with a valid job ID
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()

#     def test_successful_submission_page(self):
#         """Tests the successful submission page URL (requires login and a job_id)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('submit-application', args=['test_job_id']))  # Replace 'test_job_id' with a valid job ID
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()

#     def test_withdraw_application_page(self):
#         """Tests the withdraw application page URL (requires login and a job_id)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('withdrawapplication', args=['test_job_id']))  # Replace 'test_job_id' with a valid job ID
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()

#     def test_company_dashboard_page(self):
#         """Tests the company dashboard page URL (requires login)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('companydashboard'))
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()

#     def test_post_job_page(self):
#         """Tests the post job page URL (requires login)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('postjob'))
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()

#     def test_edit_job_page(self):
#         """Tests the edit job page URL (requires login and a job_id)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('edit-job', args=[1]))  # Replace 1 with a valid job ID
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()

#     def test_job_applications_page(self):
#         """Tests the job applications page URL (requires login)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('jobapplications'))
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()

#     def test_download_cv_page(self):
#         """Tests the download CV page URL (requires login and a filename)."""
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('download_cv', args=['test_filename.pdf']))  # Replace 'test_filename.pdf' with a valid filename
#         self.assertEqual(response.status_code, 200)
#         self.client.logout()
