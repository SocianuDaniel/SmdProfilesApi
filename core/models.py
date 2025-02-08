from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    """Mamager for users"""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must provide an email ....')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_hospitality(self, email, password=None, **extra_fields):
        user=self.create_user(email, password)
        user.level=7
        user.save(using=self._db)
        return user

    def create_shift(self, email, password=None, **extra_fields):
        user=self.create_user(email, password)
        user.level=6
        user.save(using=self._db)
        return user

    def create_assistentstoremanager(self, email, password=None, **extra_fields):
        user=self.create_user(email, password)
        user.level=5
        user.save(using=self._db)
        return user
    
    def create_storemanager(self, email, password=None, **extra_fields):
        user=self.create_user(email, password)
        user.level=4
        user.save(using=self._db)
        return user

    def create_zonemanager(self, email, password=None, **extra_fields):
        user=self.create_user(email, password)
        user.level=3
        user.save(using=self._db)
        return user

    def create_regionmanager(self, email, password=None, **extra_fields):
        user=self.create_user(email, password)
        user.level=2
        user.save(using=self._db)
        return user

    def create_owner(self, email, password=None, **extra_fields):
        user=self.create_user(email, password)
        user.level=1
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """create superusers """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.level = 0
        user.save(using=self._db)

        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    """User in the System"""
    USER_LEVEL = (
        (0,_('SUPERUSER')),
        (1,_('OWNER')),
        (2,_('REGIONMANAGER')),
        (3,_('ZONEMANAGER')),
        (4,_('STOREMANAGER')),
        (5,_('ASSISTENTSTOREMANAGER')),
        (6,_('SHIFT')),
        (7,_('HOSTESS')),
        (8,_('CREW'))
)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    level = models.IntegerField(choices=USER_LEVEL,default=8)
    owner = models.ForeignKey('self', default=None, on_delete=models.SET_DEFAULT,null=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
