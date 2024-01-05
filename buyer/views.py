from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUP, ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from car_model.models import BuyModel
# Create your views here.


def user_signup(request):
    if request.method == 'POST':
        form = SignUP(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('profile_page')
    else:
        form = SignUP()
    return render(request,'login_&_logout.html',{'form':form, 'type': 'Signup'})

def user_profie(request):
    user = request.user
    details = BuyModel.objects.filter(buyer=user)
    return render(request,'profile.html',{'detail':details})

def user_edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile_page')
    else:
        profile_form = ChangeUserForm(instance = request.user)
    return render(request, 'login_&_logout.html', {'form' : profile_form, 'type': 'Signup'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,"Logged in to account Successfully")
                login(request, user)
                return redirect('profile_page')
            else:
                messages.warning(request,"At first creat an account")
                return redirect('signup_page')
    else:
        form = AuthenticationForm()
        return render(request,'login_&_logout.html',{'form':form, 'type': 'Login'})
    

def user_logout(request):
    logout(request)
    return redirect('login_page')


