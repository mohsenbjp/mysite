from django.shortcuts import render,HttpResponse
from app1.models import Contact
from app1.forms import ContactForm,NewsletterForm
from django.contrib import messages

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
            # name=form.cleaned_data.get('name')
            form=form.save()
            form.name="unknown"
            form.save()
            messages.add_message(request, messages.SUCCESS, 'aqa shod.')
        else:
            messages.add_message(request, messages.ERROR, 'aqa nashod.')

    form=ContactForm()
    return render(request,'app1/contact.html',{'form':form})

def newsletter(request):
    if request.method == 'POST':
        form=NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'aqa shodaaa.')
        else:
            messages.add_message(request, messages.ERROR, 'aqa nashodaaa.')

        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
