from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['matricula', 'nome', 'sobrenome', 'email', 'curso', 'media']
    labels = {
      'student_number': 'Matrícula',
      'first_name': 'Nome',
      'last_name': 'Sobrenome',
      'email': 'Email',
      'curso': 'Curso',
      'media': 'Média'
    }
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'curso': forms.TextInput(attrs={'class': 'form-control'}),
      'media': forms.NumberInput(attrs={'class': 'form-control'}),
    }

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


