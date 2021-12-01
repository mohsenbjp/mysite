from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method=='POST':

            #1
            a=SignUpForm(request.POST)
            print(a)
            if a.is_valid():
                a.save()
                # email=a.cleaned_data.get('email')
                # print(email)

            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                # useremail=form.cleaned_data['email'].lower().strip()
                email=form.cleaned_data.get('email')
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user=authenticate(request,username=username,password=password,email=email)
                if user is not None:
                    login(request,user)
                    return redirect('/')
        form=AuthenticationForm()
        context={'form':form}
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=SignUpForm()
    print(form)
    context={'form':form}
    return render(request,'accounts/signup.html',context)
