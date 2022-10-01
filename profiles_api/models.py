from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        # normalized email address
        # make second part of email address all lowercase
        # but now normalize all character to lowercase
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        # make sure the password is encrypted
        # convert password into hash, never store it as plain text in database
        # make sure other people can only see the hashed password
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system"""
    # specify a email column in our UserProfile data table;
    # email is email field with a maximum length of 255 chracters
    # and make sure it's unique
    email = models.EmailField(max_length=255, unique=True)
    # specify name field
    # specify each email mathch with a name
    name = models.CharField(max_length=255)
    # determine if a user profile is activated or not
    # by default, all of then is activated (as default)
    is_active = models.BooleanField(default=True)
    # if user is a staff user
    # if to create staff user, just set default=True
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # user don't need to provide user name to login
    # only email and password is enough
    USERNAME_FIELD = 'email'
    # At minimum, user need to specify name, which is email
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
