from django.shortcuts import render
from collections import Counter

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    counts = Counter(wordlist)
    return render(request, 'count.html', {'fulltext': fulltext, 'wordlist':len(wordlist), 'counts': counts.items()})

def about(request):
    return render(request, 'about.html')