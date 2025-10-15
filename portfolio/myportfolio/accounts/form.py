from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Education
from django.contrib.auth.hashers import make_password

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'year']