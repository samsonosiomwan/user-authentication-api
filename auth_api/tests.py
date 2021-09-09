from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('auth_api:register')
GENERATE_OTP_URL = reverse('auth_api:generate-otp')
USER_LOGIN_URL = reverse('auth_api:login-token')

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class RegisterUserApiTests(TestCase):
    """Test the Auth API"""
    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'email': 'samson@gmail.com',
            'password': 'test123',
            'name': 'test name'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        # self.assertEqual(res.status_code, status.HTTP_201_CREATED)
     
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))

    def test_user_exists(self):
        """Test user exists"""

        payload = {
            'email': 'samson@gmail.com',
            'password': 'test123',
            'name': 'Test'
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        

    def test_create_user_missing_field(self):
        """Test creating user with missing field"""
        payload = {
            'email': 'samson@gmail.com',
            'password': '',
            'name': 'Test'
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
       

    def test_password_too_short(self):
        """Test that the password must be more than 5 chars"""
        payload = {
            'email': 'samson@gmail.com',
            'password': 'test',
            'name': 'T'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)


    def test_generate_otp_for_user(self):
        """Test that otp is created for user"""
        payload = {
            'email': 'samson@gmail.com',
        }
        create_user(**payload)
        res = self.client.post(GENERATE_OTP_URL, payload)

        self.assertIn('OTP', res.data)

    def test_generate_otp_no_user(self):
        """"Test that otp is not generated if user doesnt exist"""
        payload = {'email': 'samson@gmail.com'}
        res = self.client.post(GENERATE_OTP_URL, payload)

        self.assertNotIn('OTP', res.data)
        

    def test_generate_otp_missing_field(self):
        """Testing generate otp with missing field"""
        res = self.client.post(GENERATE_OTP_URL, {'email': ''})
        self.assertNotIn('token', res.data)
        

    def test_login_for_user(self):
        """Test user login"""
        payload = {
            'email': 'samson@gmail.com',
            'password': 'test'
        }
        create_user(**payload)
        user = get_user_model().objects.get(email=payload['email'])
        user.is_active = True
        user.save()
        res = self.client.post(USER_LOGIN_URL, payload)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_login_for_unverified_user(self):
        """Test login for unverified user"""
        payload = {
            'email': 'samson@gmail.com',
            'password': 'test'
        }
        create_user(**payload)
        user = get_user_model().objects.get(email=payload['email'])
        
        res = self.client.post(USER_LOGIN_URL, payload)
        self.assertNotIn('token', res.data)
       
    
    def test_user_login_missing_field(self):
        """Test user login missing field"""
        payload = {
            'email': 'samson@gmail.com',
            'password': ''
        }
        create_user(**payload)
        user = get_user_model().objects.get(email=payload['email'])
        
        res = self.client.post(USER_LOGIN_URL, payload)
        self.assertNotIn('token', res.data)
        

