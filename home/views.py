from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def quiz(request):
    return render(request, 'home/quiz_game.html')