from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import pandas as pd
from . import training


# Create your views here.
def projects(request):
    finalOutput = ''
    reqInputs = ''
    if request.method == "POST":
        file = request.FILES['myFile']
        reqInputs = request.POST.get('reqInputs', '')
        userInputs = reqInputs.split(',')
        finalOutput = training.makePrediction(file, userInputs)

    context = {'finalOutput': finalOutput,
               'reqInputs': reqInputs}
    return render(request, 'predict.html', context)

    return render(request, 'predict.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def mainPage(request):
    return render(request, 'home.html')
