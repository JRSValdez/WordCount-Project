from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordDic = {}

    for word in wordlist:
        if word in wordDic:
            wordDic[word] += 1
        else:
            wordDic[word] = 1
    
    sortedWords = sorted(wordDic.items(), key=operator.itemgetter(1), reverse = True)

    return render(request, 'countPage.html', 
                        {'fulltext': fulltext, 'numWords': len(wordlist), 'wordDic': sortedWords})