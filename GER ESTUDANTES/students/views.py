from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Student
from .forms import StudentForm

from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm, SignupForm


# Create your views here.
def index(request):
  students = Student.objects.all()

  return render(request, 'students/index.html', {
    'students': students})


def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    print(request.POST['nome'])
    if form.is_valid():
      new_matricula = request.POST['matricula']
      new_nome = request.POST['nome']
      new_sobrenome = request.POST['sobrenome']
      new_email = request.POST['email']
      new_curso = request.POST['curso']
      new_media = request.POST['media']

      new_student = Student(
        matricula=new_matricula,
        nome=new_nome,
        sobrenome=new_sobrenome,
        email=new_email,
        curso=new_curso,
        media=new_media
      )
      new_student.save()
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })


def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
              login(request, user)
              return redirect('index')
    else:
      form = LoginForm()
      return render(request, 'login.html', {'form': form})
# logout page
def user_logout(request):
    logout(request)
    return redirect('index')

# signup page
def user_signup(request):
    if request.method == 'POST':
      form = SignupForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('login')
    else:
      form = SignupForm()
      return render(request, 'students/signup.html', {'form': form})