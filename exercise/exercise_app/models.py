# location_app/models.py
from django.db import models
# from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
import uuid
# from .managers import CustomUserManager

# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(_("email address"), unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ('username', )
    
#     objects = CustomUserManager()
    
#     def __str__(self):
#         return self.email
    # my_user = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    
class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)
    curr_symbol = models.CharField(max_length=10)
    phone_code = models.CharField(max_length=10)
    # my_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)


class State(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    state_code = models.CharField(max_length=10)
    gst_code = models.CharField(max_length=10)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    city_code = models.CharField(max_length=10)
    phone_code = models.CharField(max_length=10)
    population = models.IntegerField()
    avg_age = models.FloatField()
    num_of_adult_males = models.IntegerField()
    num_of_adult_females = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
from django.db import models

# Create your models here.
