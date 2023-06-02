
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255, required=True,widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['email' , 'username' , 'password1','password2']
    


