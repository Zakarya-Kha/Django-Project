from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request, 'index.html', )

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render (request, 'counter.html', {'amount': amount_of_words})

