from django.contrib import admin
from .models import User
from books.models import Book
from publishers.models import Publisher

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Publisher)
