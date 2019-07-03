# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

import datetime

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_delete
from django.utils.timezone import utc
import random
import string
alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Numbers are not allowed.')


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            pass
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        code = ''.join(random.choices(
            string.ascii_letters + string.digits, k=16))
        extra_fields.setdefault('code', code)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    GENDER_TYPE = (('Male', 'Male'),
                   ('Female', 'Female'),
                   ('Others', 'Others')
                   )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    code = models.CharField(max_length=16, null=False,blank=False,unique=True)
    gender = models.CharField(max_length=250, choices=GENDER_TYPE)
    address = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True,
                              upload_to='media/images/user/%Y-%m-%d/')

    objects = UserManager()

    def __str__(self):
        return self.email


class AdminUser(models.Model):
    admin_user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='AdminUser')

    def __str__(self):
        return 'Admin User-{}'.format(self.admin_user.username)


class NormalUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='NormalUser')
    approved = models.BooleanField(default=False)
    parent_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='Normal_Parent_User',max_length=100)
    parent_code = models.CharField(max_length=16,unique=True,null=False,blank=False)

    def __str__(self):
    	return 'Normal User-{}'.format(self.user.username)



