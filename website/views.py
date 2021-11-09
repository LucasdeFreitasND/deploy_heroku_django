from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def pretinha(request):
    return render(request,'pretinha.html')