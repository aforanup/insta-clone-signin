from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    phone_no = models.CharField(max_length=15, blank=True)
    profile_pic = models.ImageField(
        upload_to='userProfilePic/',
        null=True, blank=True,
        verbose_name='profile picture'
    )

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profile'

    def __str__(self):
        if self.email:
            return self.username, self.email
        else:
            return self.username
