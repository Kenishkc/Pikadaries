from django.shortcuts import render,HttpResponse

# Create your views here.


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'services.html')

