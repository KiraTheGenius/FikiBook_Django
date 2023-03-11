from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (("M", 'Male'),
                      ('F', 'Female'),
                      ('N', 'Non Binary'),
                      )

    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    is_publisher = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.username
