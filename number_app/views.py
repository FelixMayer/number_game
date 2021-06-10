from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    return render(request, 'index.html')



def counting_guess(request):
    request.session['number'] = num = random.randint(1, 100)
    if 'number' > request.POST['num']:
        return redirect('/low')
    elif 'number' < request.POST['num']:
        return redirect('/high')
    else:
        return redirect('/correct')

def low(request):
    if 'number' > request.POST['num']:
        return render(request, 'low.html')
    elif 'number' < request.POST['num']:
        return redirect('/high')
    else:
        return redirect('/correct')

def high(request):
    if 'number' > request.POST['num']:
        return redirect('/low')
    elif 'number' < request.POST['num']:
        return render(request, 'high.html')
    else:
        return redirect('/correct')

def correct(request):
    return render(request, 'correct.html')
