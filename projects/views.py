from django.shortcuts import render
from django.http import HttpResponse
# from .forms import FileForm
import pandas as pd
from . import training

# Create your views here.


def projects(request):
    if request.method == "POST":
        file = request.FILES['myFile']
        reqInputs = request.POST.get('reqInputs')
        userInputs = reqInputs.split(',')
        finalOutput = training.makePrediction(file, userInputs)
        context = {'finalOutput': finalOutput}
        return render(request, 'predict.html', context)

    return render(request, 'predict.html')


def mainPage(request):
    return render(request, 'home.html')
