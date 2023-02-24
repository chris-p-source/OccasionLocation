from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):

    def create_user(self, email, firstname, lastname, username, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueErorr("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        if not firstname:
            raise ValueError("Users must have a full name")
        if not lastname:
            raise ValueError("Users must have a last name")  
        if not username:
            raise ValueError("Users must have a username")  

        user_obj = self.model(
            email = self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            username=username
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, firstname, lastname, username, password=None):
        user = self.create_user(
            email,
            firstname,
            lastname,
            username,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, firstname, lastname, username, password=None):
        user = self.create_user(
            email,
            firstname,
            lastname,
            username,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    firstname = models.CharField(max_length=20, verbose_name='First Name')
    lastname = models.CharField(max_length=20, verbose_name='Last Name')
    mobilenum = models.CharField(max_length=11, verbose_name='Mobile Number')
    username = models.CharField(max_length=255, unique=True, verbose_name='Username')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['firstname', 'lastname', 'username']

    objects = UserManager()

    def __str__(self):
        return self.email


    def get_first_name(self):
        if self.firstname:
            return self.firstname
        return self.email

    def get_last_name(self):
        if self.lastname:
            return self.lastname
        return self.email


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    



