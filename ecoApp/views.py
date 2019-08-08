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
    return redirect('event_information')

def signin(request):
    alert = False
    if request.method == 'POST':
        user = User()
        try:
            user = User.objects.create_user(username = request.POST.get('username'),
                                            password = request.POST.get('password'))
            message = 'Registrado correctamente'
            alert = True
        except:
            messages.success(request, 'Ocurrio un error en el registro, intente mas tarde')
            alert = False
            variables = {'alert': alert}
            return render(request, 'ecoApp/signin.html', variables)
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('firstName')
        user.last_name = request.POST.get('lastName')
        user.profile.rut = request.POST.get('rut')
        user.profile.dv = request.POST.get('dv')
        user.profile.birth_date = request.POST.get('birthdate')
        user.profile.address = request.POST.get('address')
        user.profile.phone_number = request.POST.get('phoneNumber')
        user.profile.available = True
        messages.error(request, message)
        user.save()
    variables = {'alert': alert}
    return render(request, 'ecoApp/signin.html', variables)

def curriculum(request):
    return render(request, 'ecoApp/curriculum.html', {})

def profile(request):
    return render(request, 'ecoApp/profile.html', {})
