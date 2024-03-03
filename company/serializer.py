

# from .task import send_html_email
from .tasks import send_mail_func
from .models import EmployeDetail
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import logging
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import EmployeDetail
from django.contrib.auth.hashers import make_password, check_password

logger = logging.getLogger(__name__)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        try:
            employee = EmployeDetail.objects.get(email=email)
        except EmployeDetail.DoesNotExist:
            raise serializers.ValidationError('User with this email does not exist.')
        is_correct = check_password(password, employee.password)
        if is_correct:
            password=employee.password
        else:
            password=password
        if email and password:
            user = EmployeDetail.objects.get(email=email, password=password)
           
            if user:
                refresh = RefreshToken.for_user(user)
                return {
                    'tokens': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        "role":user.role
                    }
                }
            else:
                raise serializers.ValidationError('Invalid email or password')
        else:
            raise serializers.ValidationError('Email and password are required fields')
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = EmployeDetail
        fields = '__all__'

    def create(self, validated_data):
        user = EmployeDetail.objects.create(
            firstname=validated_data['firstname'],lastname=validated_data['lastname'],
            email=validated_data['email'],employee_code=validated_data['employee_code'],
            contact_no=validated_data['contact_no'],department=validated_data['department'],
            role=validated_data['role'],
        )
        user.set_password(validated_data['password'])
        try:
            send_mail_func.delay(validated_data['email'],validated_data['password'])
        except Exception as e:
            # Handle the exception, log it, or perform any necessary actions
            pass
            # send_html_email.delay(email, username, password)
        user.save()

        return user