from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from company.models import EmployeDetail
import jwt

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            decoded_token = jwt.decode(token, options={"verify_signature": False})
            print("Token ID:", token)
        return True 
       
        
        # user = EmployeDetail.objects.get(email=request.data['email']).role
        # if user == "admin":
        #     return True
        # elif user == "employees":
        #     return request.method in ['GET', 'PUT']
        # else:
        #     raise PermissionDenied("You do not have permission to perform this action.")
        
        # return (request.user.usertype == "admin" or(request.user.usertype == "employees" and (request.method=='GET' or request.method=='PUT')))