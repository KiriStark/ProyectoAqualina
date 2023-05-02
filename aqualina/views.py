from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError

# Create your views here.
def home(request):
    
    return render(request, 'index.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Registrar usuario
                user = User.objects.create_user(username=request.POST['username'], 
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Contrasenas no coinciden'
                })
    
def sucursales(request):
    return render(request, 'Sucursales.html')

def contactanos(request):
    return render(request, 'contactanos.html')

def signout(request):
    logout(request)
    return redirect('/')

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], 
                                     password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o contrasena incorrectos'
            })
        else:
            login(request, user)
            return redirect('/')
