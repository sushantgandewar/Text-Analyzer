#Imports
from django.http import HttpResponse
from django.shortcuts import render

#Main Function to render home page
def home(request):
    #params = {'name':'SSG','invite':'Welcome'}

    return render(request,'home.html')

#Function Logic and output page
def analyze(request):
    #Getting text
    djtext = request.POST.get('text','default')

    #Getting values from Checkboxes
    removepunc = request.POST.get('removepunc','off')
    allcaps = request.POST.get('allcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')

    #Check Box is ON
    #Remove Punctuations
    if removepunc == "on":
        #Analyze text
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctations', 'analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)

    #All Letter Capitalize
    if allcaps == "on":
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized All Text', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    #new line remover
    if newlineremover == "on":
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'New Lines Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    #Space remover
    if spaceremover == "on":
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index-1] == " " and  djtext[index] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

     # Character counter
    if charcount == "on":
        analyzed = 'Count is '
        count = 0
        for char in djtext:
            count = count + 1

        analyzed = analyzed + str(count)
        params = {'purpose': 'Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if removepunc != "on" and allcaps != "on" and newlineremover != "on" and spaceremover != "on" and charcount != "on":
        return HttpResponse("Opps! You haven't selected any operation from the list. Please select any operation to perform any changes.")

    return render(request, 'analyze.html', params)