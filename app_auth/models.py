from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from app_auth.managers import CustomUserManager
from app_shared.models import BaseModel


class Authority(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    action = models.CharField(max_length=30, null=True, unique=True)
    resource = models.CharField(max_length=50, null=True, unique=True)

    class Meta:
        db_table = 'authorities'


class Role(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=50, null=True, unique=True)
    authorities = models.ManyToManyField(Authority, blank=True, db_table='role_authorities')

    class Meta:
        db_table = 'roles'


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    roles = models.ManyToManyField(Role, blank=True, db_table='user_roles')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name')

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
