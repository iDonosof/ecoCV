from django.shortcuts import render

# Create your views here.
def event_information(request):
    return render(request, 'ecoApp/event_information.html',{})

def login(request):
    return render(request, 'ecoApp/login.html', {})

def signin(request):
    return render(request, 'ecoApp/signin.html', {})

def curriculum(request):
    return render(request, 'ecoApp/curriculum.html', {})

def profile(request):
    return render(request, 'ecoApp/profile.html', {})
