from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save

# Create your models here.
class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

def create_profile(send, **kwargs):
    if kwargs['created']:
        user_profile = CustomUser.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
