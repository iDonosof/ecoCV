from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.template.context_processors import request
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def event_information(request):
    return render(request, 'ecoApp/event_information.html',{})

def login_view(request):
    alert = True
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('event_information'))
        else:
            alert = False
            messages.error(request, 'Error al iniciar sesion ☹️')
    variables = {'alert': alert}
    return render(request, 'ecoApp/login.html', variables)

@login_required(login_url = 'login')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')

def signin(request):
    return render(request, 'ecoApp/signin.html', {})

def curriculum(request):
    return render(request, 'ecoApp/curriculum.html', {})

def profile(request):
    return render(request, 'ecoApp/profile.html', {})
