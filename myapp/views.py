from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'Home.html')

def services(request):
    return HttpResponse('services app')

def signup(request):
    if request.method == 'GET':
        return render(request, 'Signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('Home')
            except IntegrityError:
                return render(request, 'Signup.html', {
                    'form': UserCreationForm,
                    "error": 'User already exist'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })

def signin(request):
    if request.method == 'GET':
        return render(request, 'Signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'Signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('Home')
        
@login_required
def signout(request):
    logout(request)
    return redirect('Home')