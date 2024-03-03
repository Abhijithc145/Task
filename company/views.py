from django.shortcuts import render

from common.helper.permitions import UserPermission
from .tasks import send_mail_func
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework import status
from django.contrib.auth.hashers import make_password
# from common.helper.error_handling import handle_exceptions
from rest_framework_simplejwt.tokens import AccessToken
from .models import EmployeDetail
from .serializer import *
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
import jwt


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        print(password)

        if not email or not password:
            raise ValidationError("Must include 'email' and 'password'.")

        return super().post(request, *args, **kwargs)
    
class AdminRegisterView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        request.data['role']="admin"
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class UserRegisterView(APIView):
    # permission_classes = (UserPermission,)
    serializer_class = RegisterSerializer
    def get(self, request, *args, **kwargs):
        queryset = EmployeDetail.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request, *args, **kwargs):
        print("sdlkfaksdh==>",request.headers)
        request.data['role']="employees"
        queryset = EmployeDetail.objects.all()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class Userdetails(APIView):
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def get_object(self, id):
        try:
            return EmployeDetail.objects.get(id=id)
        except EmployeDetail.DoesNotExist:
            raise Http404

    def get(self, request, id, *args, **kwargs):
        user = self.get_object(id)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def put(self, request, id, *args, **kwargs):
        user = self.get_object(id)
        serializer = self.serializer_class(user, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET'])
# def my_api_view(request):
#     send_mail_func.delay()
#     return Response({"message": "Hello, world!"})
