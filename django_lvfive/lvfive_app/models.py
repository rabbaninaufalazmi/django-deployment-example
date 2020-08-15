from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class UserInput(models.Model):
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     email = models.EmailField(max_length=255, unique=True)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional classess
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.username
