from django.shortcuts import render,HttpResponse
from app1.models import Contact
from app1.forms import ContactForm,NewsletterForm

# Create your views here.
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

def index(request):
    return render(request,'app1/index.html')

def about(request):
    return render(request,'app1/about.html')

def elements(request):
    return render(request,'app1/elements.html')

def contact(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form=ContactForm()
    return render(request,'app1/contact.html')

def newsletter(request):
    if request.method == 'POST':
        form=NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
