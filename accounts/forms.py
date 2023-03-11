from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_publisher')


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'gender', 'avatar')
