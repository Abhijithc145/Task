from django.urls import path
from .import views
from .views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    
    path('login/',MyTokenObtainPairView.as_view(),name='login'),
    path('refresh_token/',TokenRefreshView.as_view(),name='refresh_token'),
    path('admin_register/',AdminRegisterView.as_view(),name='tokenregister'),
    path('user_register/',UserRegisterView.as_view(),name='tokenregister'),
    path('user_register/<uuid:id>/', Userdetails.as_view(), name='user-details'),
    
   
    
]