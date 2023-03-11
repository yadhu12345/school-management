from dataclasses import fields
from django import forms
from .models import *

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = ('username','password','school')
        widgets = {
                'username'            : forms.TextInput(attrs={'class':'form-control', 'id':'username'}),
                'password'            : forms.PasswordInput(attrs={'class':'form-control', 'id':'password'}),
                'school'          : forms.Select(attrs={'class':'form-control', 'id':'courseid'}),
        }

class AdminregForm(forms.ModelForm):
    class Meta:
        model = login
        fields = ('username','password','school')
        widgets = {
                'username'            : forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
                'password'            : forms.PasswordInput(attrs={'class':'form-control', 'id':'examid'}),
                'school'          : forms.Select(attrs={'class':'form-control', 'id':'courseid'}),
        }

class subjectForm(forms.ModelForm):
    class Meta:
        model = subject
        fields = ('subject_name','description')
        widgets = {
            'subject_name': forms.TextInput(attrs={'class':'form-control', 'id':'subjectid'},),
            'description' : forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            
        }

class StudentLoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = ('username','password','school')
        widgets = {
                'username'            : forms.TextInput(attrs={'class':'form-control', 'id':'username'}),
                'password'            : forms.PasswordInput(attrs={'class':'form-control', 'id':'password'}),
                'school'          : forms.Select(attrs={'class':'form-control', 'id':'school'}),
        }

class studentinfoForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ('user','name','class_name','section','age','gender','admissionid','guardian_name')
        widgets = {
            'user': forms.Select(attrs={'class':'form-control', 'id':'subjectid'},),
            'name' : forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'class_name': forms.TextInput(attrs={'class':'form-control', 'id':'subjectid'},),
            'section': forms.TextInput(attrs={'class':'form-control', 'id':'subjectid'},),
            'age' : forms.NumberInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'admissionid': forms.TextInput(attrs={'class':'form-control', 'id':'subjectid'},),
            'guardian_name': forms.TextInput(attrs={'class':'form-control', 'id':'subjectid'},),
            'gender' : forms.Select(attrs={'class':'form-control', 'id':'descriptionid'}),
        }

class staffinfoForm(forms.ModelForm):
    class Meta:
        model = staff
        fields = ('user','name','staff_id','age','joined_date','gender',)
        widgets = {
            'user': forms.Select(attrs={'class':'form-control', 'id':'subjectid'},),
            'name' : forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'staff_id': forms.TextInput(attrs={'class':'form-control', 'id':'subjectid'},),
            'age' : forms.NumberInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'joined_date': forms.SelectDateWidget(attrs={'class':'form-control', 'id':'subjectid'}),
            'gender' : forms.Select(attrs={'class':'form-control', 'id':'descriptionid'}),
        }

class resultForm(forms.ModelForm):
    class Meta:
        model = results
        fields = ('student_id','subject','total_score','obtained_score')
        widgets = {
            'student_id': forms.Select(attrs={'class':'form-control', 'id':'subjectid'}),
            'subject': forms.Select(attrs={'class':'form-control', 'id':'subjectid'},),
            'total_score': forms.NumberInput(attrs={'class':'form-control', 'id':'total_score'},),
            'obtained_score' : forms.NumberInput(attrs={'class':'form-control', 'id':'obtained_score'}),
            
        }