import django.contrib
from core_root_api.security import base_url
from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import random
import requests
from core_root_api.security.user.models import CompanyProfile
import string
from django.views import View
from rest_framework.response import Response
# import resend
from core_root_api.security.auth.utils import generate_token
from django.utils.encoding import force_bytes,DjangoUnicodeDecodeError,force_str
from rest_framework.viewsets import ViewSet
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from core_root_api.security.auth.serializer.register import AdminRegisterSerializer,RegisterSerializer

# the future.
from core_root_api.security.user.models import User
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
# from core.wallet.models import UsdModel

from core_root_api.security.auth.serializer.verify_serializer import VerifySerializer

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

if not settings.configured:
    settings.configure(
        EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend',
        EMAIL_HOST='mail.finderskeepers.ai',
        EMAIL_PORT=587,  # Using TLS port
        EMAIL_HOST_USER='support@finderskeepers.ai',
        EMAIL_HOST_PASSWORD='L4h6b##+g%db',
        EMAIL_USE_TLS=True,  # Enable TLS
        EMAIL_USE_SSL=False,  # Ensure SSL is disabled
    )

def send_welcome_email(message_body, company_name, support_email, reciever_email):
    # Define the context for your email template
    context = {
        'message_body': message_body,
        'company_name': company_name,
        'support_email': support_email,
    }

    # Render the HTML email content from the template named 'email_template.html'
    html_content = render_to_string('email_template.html', context)

    # Create the EmailMessage object
    email = EmailMessage(
        subject='Onboarding Message',
        body=html_content,
        from_email=settings.EMAIL_HOST_USER,
        to=[reciever_email],
        bcc=['bcc@anotherbestuser.com'],
        reply_to=['whoever@itmaybe.com'],
    )

    # Specify that the email body is HTML
    email.content_subtype = 'html'

    # Send the email
    email.send()


# Example usage:
# send_welcome_email(
#     message_body="Welcome to our service! We're excited to have you on board.",
#     company_name="Finders Keepers",
#     support_email="support@finderskeepers.ai",
#     reciever_email="recipient@example.com"
# )


@swagger_auto_schema(
    request_body=AdminRegisterSerializer,
    responses={200: AdminRegisterSerializer}
)

class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def generate_random_link(self,length=20):
        # Define the characters allowed in the link
        characters = string.ascii_letters + string.digits

        # Generate a random link by selecting characters randomly
        random_link = ''.join(random.choice(characters) for _ in range(length))

        return random_link
    
    def create(self, request, *args, **kwargs):
        try:
            print(request.data)
            serializer = self.serializer_class(data=request.data)
            email=str(serializer.initial_data['email'])
            email_user=email
        
            # print(serializer.initial_data['password'])
            password_length=int(len(serializer.initial_data['password']))
            print(password_length)
            print(type(password_length))
            error_list=[]
            if not serializer.is_valid():
                print("not valid")
                if User.objects.filter(email=email).exists():
                    # return Response({'message':'User with this email already exists','error':True,'field':'email'},status=status.HTTP_403_FORBIDDEN)
                    email_error='User with this email already exists'
                    error_list.append(email_error)
                if password_length<8:
                    # print(password_length)
                    # print(type(password_length))
                    password_error='Password should be at least 8 characters'
                    error_list.append(password_error)
                
                
                if str(serializer.initial_data['confirm_password'])is not str(serializer.initial_data['password']):
                    password_mismatch_error='Password mismatch for confirm password'
                
                    error_list.append(password_mismatch_error)
                
                error_list=error_list
                return Response({'error_message':error_list[0],'status':False},status=status.HTTP_406_NOT_ACCEPTABLE)
            # if serializer.is_valid():
            else:
                

                print("validated good")
                

                
                # unassigned_keys=OpenAiAdminModel.objects.filter(assigned=False).first()

                # if unassigned_keys:
                #     unassigned_keys.assigned=True

                #     open_api_key=unassigned_keys.open_ai_key

                #     unassigned_keys.save()

                #     OpenAiUserModel.objects.create(user=user,custom_user_key_id=unassigned_keys.custom_user_key_id,open_ai_key=open_api_key,time_of_assiging=timezone.now())
                # User.objects.get(email=request.user.email).is_active=False
                # import resend
                # resend.api_key = "re_QPQ9uUgC_AQgi1DuGsDWDMTxxUyo88XPi"
                # from core_app_root.security.base_url import main_url
                # from core_app_root.security import base_url
                # full_url=main_url+self.generate_random_link()
                
                # r = resend.Emails.send({
                # "from": "send@christiankelechieze.com",
                # "to": f"{email}",
                # "subject": "Account Verification",
                # "html": f"""<p>Congrats on Signing up <strong> with Codeblaze Academy</strong> click this link <a href="{base_url.main_url}account/verify/{email}/">{self.generate_random_link()}</a> to verify your account </p>"""
                # })
                # import random
                # activation_code=random.randint(1000, 9999)
                # import smtplib
                # from email.mime.multipart import MIMEMultipart
                # from email.mime.text import MIMEText
            
                # # Define the email details
                
                message = f"""
                Dear {serializer.validated_data['full_name']},
                Subject: Welcome to Xpress Job Connect – Your Global Gateway to Career Opportunities!

                Dear [User Name],

                Congratulations on joining Xpress Job Connect! We’re thrilled to have you on board and can’t wait for you to explore everything our platform has to offer.

                Xpress Job Connect is more than just a job portal – it’s a cutting-edge solution designed to connect job seekers with opportunities from around the globe. Here’s how we empower you to take the next step in your career:

                Global Job Connectivity
                Our platform connects you with employers and job opportunities worldwide, breaking down geographical barriers and expanding your horizons.

                Real-Time Notifications
                Stay updated with instant alerts for new job postings, interviews, and career events tailored to your preferences.

                Advanced Search & Matching
                Utilize our intelligent search filters and matching algorithms to find positions that align with your skills, experience, and career aspirations.

                User-Friendly Interface
                Enjoy a seamless experience with our intuitive design, making it easier than ever to navigate job listings, submit applications, and track your progress.

                Verified Employers & Secure Platform
                We prioritize your safety by ensuring all job listings and employer profiles are thoroughly verified for authenticity and security.

                Personalized Career Resources
                Access exclusive career advice, resume tips, and interview preparation guides to help you put your best foot forward.

                At Xpress Job Connect, our mission is to empower you to find the perfect job and accelerate your career growth. We’re committed to supporting you every step of the way.

                If you have any questions or need assistance getting started, please don’t hesitate to reach out to our friendly support team. We’re here to help you succeed!

                Welcome to the Xpress Job Connect family – let’s connect you to your future!

                Best regards,

                Favour 
                Xpress Job Connect Team
                """
                send_welcome_email(message,"Xpress Job Connect",str("support@finderskeepers.ai"),serializer.validated_data['email'])                 
                # receiver_email = email
                # subject = "Account Activation Code"
                # # body = f"Enter the four digit code sent to you here in your Blanc Exchange application to continue with account registration completion   {activation_code} , you can copy and paste the activation code"
                # mail_body={
                #     "userEmail":receiver_email,
                #     "text":message,
                #     "subject":"New User Registration",
                #     "title":f"Account Created Successfully"
                # }
                
                # response_mail=requests.post(url="https://zenia-email-api.vercel.app/api/v1/register_email",json=mail_body)
                
                # if str(response_mail.json()['msg'])=="You should receive an email from us":
                    
                user=serializer.save()
                # user.is_active=False
                user.is_confirmed=True
                user.save()
            
                
            
                serializer_data = serializer.data.copy()  # Create a copy of the serializer data
                serializer_data.pop('confirm_password', None) 
                
                return Response({
                    "user": serializer_data,
                    "status":True,
                    "detail":"Account creation successful, check email to get your authentication code"
                }, status=status.HTTP_201_CREATED)   
            
        
            return Response({
                    "user": serializer_data,
                    "status":True,
                    "detail":"Account creation successful, check email to get your authentication code"
            }, status=status.HTTP_201_CREATED)   
    
        except Exception as e:
            return Response({
                    
                        "status":False,
                        "detail":f"Network error ,try again later {e}"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
#         serializer = self.serializer_class(data=request.data)
#         email=str(serializer.initial_data['email'])
       
#         # print(serializer.initial_data['password'])
#         password_length=int(len(serializer.initial_data['password']))
#         print(password_length)
#         print(type(password_length))
#         error_list={}
#         if not serializer.is_valid():
#             print("not valid")
#             if User.objects.filter(email=email).exists():
#                 # return Response({'message':'User with this email already exists','error':True,'field':'email'},status=status.HTTP_403_FORBIDDEN)
#                 error_list['email_error']='User with this email already exists'
#             if password_length<8:
#                 # print(password_length)
#                 # print(type(password_length))
#                 error_list['password_error']='Password should be at least 8 characters'

            
#             # if User.objects.filter(username=username).exists():
#             #     error_list['username_error']='username exist'
#             # if str(serializer.initial_data['confirm_password'])!=str(serializer.initial_data['password']):
#                 # error_list['password_mismatch_error']='Password mismatch for confirm password'
#             if str(serializer.initial_data['password'])!=str(serializer.initial_data['confirm_password']):
#                 error_list['error_msg']="Password mismatch"
#             # error_list['error_msg']='Could not create account'
#             error_list['status']=False
#             return Response({'error_list':error_list},status=status.HTTP_406_NOT_ACCEPTABLE)
#         # if serializer.is_valid():
#         else:
            

#             print("validated good")
#             email=serializer.validated_data['email']

#             user=serializer.save()

#             refresh = RefreshToken.for_user(user)
          
#             res = {
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#             'user_email':str(serializer.validated_data['email'])
#             }
#             serializer_data = serializer.data.copy()  # Create a copy of the serializer data
#             serializer_data.pop('confirm_password', None) 
#             return Response({
#                 "user": serializer_data,
#                 "refresh": res["refresh"],
#                 "token": res["access"],
#                 'user_email':res['user_email'],
#                 "is_active":True,
#                 "status":True,
#                 "success_msg":"Account creation successful, check email to verify your account"
#             }, status=status.HTTP_201_CREATED)   
            

class AdminRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = AdminRegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    def create(self, request, *args, **kwargs):
       
        serializer = self.serializer_class(data=request.data)
        email=str(serializer.initial_data['email'])
        password_length=int(len(serializer.initial_data['password']))
        print(password_length)
        print(type(password_length))
        error_list={}
        if not serializer.is_valid():
            print("not valid")
            if User.objects.filter(email=email).exists():
                error_list['email_error']='User with this email already exists'
            if password_length<8:
                error_list['password_error']='Password should be at least 8 characters'
            if User.objects.filter(username=username).exists():
                error_list['username_error']='username exist'
            if str(serializer.initial_data['password'])!=str(serializer.initial_data['confirm_password']):
                error_list['error_msg']="Password mismatch"
            error_list['status']=False
            return Response({'error_list':error_list},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            print("validated good")
            email=serializer.validated_data['email']
            user=serializer.save()
            user.is_superuser=True
            user.is_staff=True
            user.save()
    
            refresh = RefreshToken.for_user(user)

            CompanyProfile.objects.create(user=user,company_phone_number=serializer.validated_data['company_phone_number'],company_name=serializer.validated_data['company_name'],company_url=serializer.validated_data['company_url'],address=serializer.validated_data['company_address'])
            
            res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            'user_email':str(serializer.validated_data['email'])
            }
            serializer_data = serializer.data.copy()  # Create a copy of the serializer data
            serializer_data.pop('confirm_password', None) 
            return Response({
                "user": serializer_data,
                "refresh": res["refresh"],
                "token": res["access"],
                'user_email':res['user_email'],
                "is_active":True,
                "status":True,
                "success_msg":"Account creation successful, check email to verify your account"
            }, status=status.HTTP_201_CREATED)   
            
    # return Response({'error': 'No unassigned keys available.'}, status=status.HTTP_404_NOT_FOUND)
    # else:
    #     return Response({"error":"User with this Api have an existing api key"},status=status.HTTP_403_FORBIDDEN)
class ActivateAccountView(viewsets.ModelViewSet):
    serializer_class = VerifySerializer
    permission_classes=[AllowAny]
    queryset=User.objects.all()
    http_method_names=['get']
    @action(detail=False, url_path='verify/(?P<email>[^/]+)')
    def verify_account(self, request, email=None):
        # Your logic to activate the account using the email parameter
        user = get_object_or_404(User, email=email)
        
        # Update the _active field to True
        user.is_active=True
        
        user.save()
        return HttpResponseRedirect('https://codeblazeacademy-app.vercel.app/signin')
    