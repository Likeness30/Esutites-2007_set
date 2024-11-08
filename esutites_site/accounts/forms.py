from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['reg_number', 'nickname', 'date_of_birth', 'address', 'resident_base',
                  'phone_number', 'reference_name', 'reference_number', 'profile_picture']
