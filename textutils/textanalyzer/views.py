# I have created this file - Arjun
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def analyze(request):
    '''function to analyze the text input given by user'''

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
    purpose = ""
    if isRemovePunc == 'on':
        purpose += "punctuations removed"
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        djtext = analyzed

    if isCap == 'on':
        purpose += (", capitalized all characters" if isRemovePunc == 'on' else "capitalized all characters")
        analyzed = ""
        for char in djtext:
            if char in djtext:
                analyzed += char.upper()
        djtext = analyzed

    if isNewLineRemove == 'on':
        purpose += (", new lines removed" if isRemovePunc == 'on' or isCap == 'on' else "new lines removed")
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        djtext = analyzed

    if isSpaceRemove == 'on':
        purpose += (", extra spaces removed" if isRemovePunc == 'on' or isCap == 'on' or isNewLineRemove == 'on' else "extra spaces removed")
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzed += char
        djtext = analyzed

    if isCharCount == 'on':
        purpose += (", number of characters counted" if isRemovePunc == 'on' or isCap == 'on' or isNewLineRemove == 'on' or isSpaceRemove == 'on' else "extra spaces removed")
        analyzed = f"number of characters = {len(djtext)}"
        djtext = f"Text = {djtext} and {analyzed}"


    if(isRemovePunc == 'off' and isSpaceRemove =='off' and isCap == 'off' and isNewLineRemove == 'off' and isCharCount == 'off'):
        return HttpResponse("<h1>Error</h1>")

    params = {'analyzedtext': djtext, 'purpose': purpose}
    return render(request, "analyze.html", params)




