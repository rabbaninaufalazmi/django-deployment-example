from django import forms
from .models import UserProfileInfo
# from .models import UserInput
from django.core import validators
from django.contrib.auth.models import User

# class NewUserForm(forms.ModelForm):
#     botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0,"Gotcha BOT!")])
#     class Meta:
#         model = UserInput
#         fields = "__all__"

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
