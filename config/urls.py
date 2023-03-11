from django.contrib import admin
from django.urls import path, include
from accounts.views import home
from publishers.views import AddPublisherAPIView
from books.views import AddBookAPIView, BooksView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', include('accounts.urls')),
    path('', include("django.contrib.auth.urls")),
    path('submit_publisher/', AddPublisherAPIView.as_view(), name='submit_publisher'),
    path('submit_book/', AddBookAPIView.as_view(), name='submit_book'),
    path('books/', BooksView.as_view(), name='books')
]
