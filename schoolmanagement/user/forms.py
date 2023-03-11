from dataclasses import fields
from django import forms
from smsapp.models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = ('username','password','school')
        widgets = {
                'username'            : forms.TextInput(attrs={'class':'form-control', 'id':'username'}),
                'password'            : forms.PasswordInput(attrs={'class':'form-control', 'id':'password'}),
                'school'          : forms.Select(attrs={'class':'form-control', 'id':'school'}),
        }
    
class userregForm(forms.ModelForm):
    class Meta:
        model = login
        fields = ('username','password','school')
        widgets = {
                'username'            : forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
                'password'            : forms.PasswordInput(attrs={'class':'form-control', 'id':'examid'}),
                'school'          : forms.Select(attrs={'class':'form-control', 'id':'courseid'}),
        }