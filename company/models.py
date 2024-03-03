from django.db import models
import uuid

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

ROLES = (
    ('employees', 'Employees'),
    ('admin', 'Admin'),
)

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.BooleanField(blank=False, null=False, default=True)
    deleted_at = models.DateTimeField(
        "Deleted at", auto_now=False, blank=True, null=True
    )
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        abstract = True

        indexes = [
            models.Index(
                fields=[
                    "status",
                ]
            ),
        ]

class EmployeDetail(BaseModel):
    email = models.EmailField(unique=True, blank=True,null=True)
    firstname = models.CharField(max_length=100, blank=True,null=True)
    password = models.CharField(max_length=100, blank=True,null=True)
    lastname = models.CharField(max_length=100, blank=True,null=True)
    employee_code = models.CharField(max_length=20, unique=True)
    contact_no = models.CharField(max_length=15, blank=True,null=True)
    department = models.CharField(max_length=100, blank=True,null=True)
    role = models.CharField(max_length=20, choices=ROLES, default='employees')
    REQUIRED_FIELDS = [] # Remove 'email' from the REQUIRED_FIELDS
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        
    def __str__(self):
        return self.email

