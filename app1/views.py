from django.shortcuts import render,HttpResponse

# Create your views here.
from django.http import HttpResponse,JsonResponse

def index(request):
    return render(request,'app1/index.html')

def about(request):
    return render(request,'app1/about.html')

def elements(request):
    return render(request,'app1/elements.html')

def contact(request):
    return render(request,'app1/contact.html')
