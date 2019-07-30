from django.shortcuts import render


# Create your views here.
def event_information(request):
    return render(request, 'ecoApp/event_information.html',{})