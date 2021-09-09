import pyotp
import base64
from datetime import datetime


from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import permissions

from auth_api.serializers import UserSerializer, GenerateOTPSerializer, \
    VerifyOTPSerializer, LoginTokenSerializer
from .utils import Util


EXPIRY_TIME = 1000


class GenerateKey:
    """Generate key using user email and random str"""
    @staticmethod
    def return_value(email):
        return str(email) + str(datetime.date(datetime.now())) + "abcd"


class RegisterUserView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    """Create new user in the system"""
    serializer_class = UserSerializer


class GenerateOTPView(APIView):
    """Generate OTP for verification"""
    serializer_class = GenerateOTPSerializer
    
    def post(self, request):
        email = request.data.get('email')
        try:
            user = get_user_model().objects.get(email=email)
        except ObjectDoesNotExist:
            return Response({"message":"User does not exist"}, status=404)
        
        if user.is_active == False:
            keygen = GenerateKey().return_value(email)
            user.otp_key = keygen
            user.save()

            key = base64.b32encode(keygen.encode())
            OTP = pyotp.TOTP(key, interval=EXPIRY_TIME )

            token=OTP.now()
            email_body=f'Hi{user.email}\n Please copy the code below to verify your email \n {token}'
            data={'email_body':email_body,'to_email':[user.email],'email_subject':'Verify your email'}
            Util.send_email(data)

            return Response({"OTP": OTP.now()}, status=201)
        else:
            return Response({"message": "Your account is active already, proceed to login"}, status=200)


    

class VerifyOTPView(APIView):
    """Verify generated OTP"""
    serializer_class = VerifyOTPSerializer

    # @staticmethod
    def post(self, request):
        email = request.data.get('email')
        otp_code = request.data.get('otp_code')
        try:
            user = get_user_model().objects.get(email=email)
        except ObjectDoesNotExist:
            return Response({"message":"User does not exist"}, status=404)
        
        key = base64.b32encode(user.otp_key.encode()) 
        OTP = pyotp.TOTP(key, interval=EXPIRY_TIME)
        if OTP.verify(otp_code):
            user.is_active = True
            user.save()
            return Response({"message": "Registration completed successfully, proceed to login"}, status=200)
        else:
            return Response({"message": "OTP is wrong/expired"}, status=400)
        

class LoginTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = LoginTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

