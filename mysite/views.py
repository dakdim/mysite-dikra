
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')



def ex1(request):
    sites = ['''<h1>For Entertainment  </h1> <a href="https://www.youtube.com/"> Youtube Videos</a> ''',
             '''<h1>For Interaction  </h1> <a href="https://www.facebook.com/"> Facebook</a> ''',
             '''<h1>For Insight  </h1> <a href="https://www.ted.com/talks"> Ted Talks</a> ''',
             '''<h1>For Internship  </h1> <a href="https://www.internshala.com">Internship</a> ''']
    return HttpResponse((sites))

def analyze(request):
   
    djtext = request.POST.get('text', 'default')

    
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

   
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                print(djtext)
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            print(djtext)

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
                print(djtext)

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
        

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
                

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
    if(removepunc!='on'and fullcaps!='on'and newlineremover!='on'and extraspaceremover!='on'):
        return HttpResponse("Try again with the listed operations")
    
    return render(request, 'analyze.html', params)



