from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class StudentUserForms(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your UserName'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter your Age'}))
    class_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Class Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Confirm Password'}))

    class Meta: 
        model = User
        fields=[
            'username',
            'age',
            'class_name',
            'email',
            'password1',
            'password2'
        ]
     