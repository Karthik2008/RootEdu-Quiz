from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'quiz/home.html')

def contact(request):
    return render(request, 'quiz/contact.html')

def quizlist(request):
    return render(request, 'quiz/list-quiz.html')

def linuxquiz(request):
    return render(request, 'quiz/linux-quiz.html')

def correct(request):
    return render(request, 'quiz/correct.html')

def wrong(request):
    return render(request, 'quiz/wrong.html')