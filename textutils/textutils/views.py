# I have created this file - Arjun
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def analyze(request):
    # get text
    djtext = request.POST.get('text', 'default')

    # get checkbox values
    isRemovePunc = request.POST.get('removepunc', 'off')
    isCap = request.POST.get('capitalize', 'off')
    isSpaceRemove = request.POST.get('spaceremove', 'off')
    isNewLineRemove = request.POST.get('newlineremove', 'off')
    isCharCount = request.POST.get('charcount', 'off')

    # see which checkboxes are on and analyse text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if isRemovePunc == 'on':
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        djtext = analyzed

    if isCap == 'on':
        analyzed = ""
        for char in djtext:
            if char in djtext:
                analyzed += char.upper()
        djtext = analyzed

    if isNewLineRemove == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        djtext = analyzed

    if isSpaceRemove == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzed += char
        djtext = analyzed

    if isCharCount == 'on':
        analyzed = f"number of characters = {len(djtext)}"
        djtext = f"Text = {djtext} and {analyzed}"


    if(isRemovePunc == 'off' and isSpaceRemove =='off' and isCap == 'off' and isNewLineRemove == 'off' and isCharCount == 'off'):
        return HttpResponse("<h1>Error</h1>")

    params = {'analyzedtext': djtext}
    return render(request, "analyze.html", params)


# def capfirst(request):
#     return HttpResponse("<a href='http://127.0.0.1:8000'>Back</a><h1>Capitalize first</h1>")
#
# def newlineremove(request):
#     return HttpResponse("<a href='http://127.0.0.1:8000'>Back</a><h1>Remove new line</h1>")
#
# def spaceremove(request):
#     return HttpResponse("<a href='http://127.0.0.1:8000'>Back</a><h1>Remove space</h1>")
#
# def charcount(request):
#     return HttpResponse("<a href='http://127.0.0.1:8000'>Back</a><h1>Count character</h1>")

