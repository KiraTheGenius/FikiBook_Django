from django.db import models
from accounts.models import User
from publishers.models import Publisher


class Book(models.Model):
    name = models.CharField(max_length=100)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    publication_date = models.DateField()
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
