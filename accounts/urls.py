from django.urls import path
from .views import signup, profile
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
