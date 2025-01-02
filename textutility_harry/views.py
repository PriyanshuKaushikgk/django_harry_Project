# This is creater by - Priyanshu

from django.http import HttpResponse
# from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('''<h1>Hello Priyanshu</h1> <a href = "https://www.google.com/">Google</a>''')
    # return HttpResp onse('''<h1>kaushik</h1> <a href = "http://www.facebook.com/">facebook</a>''')

def about(request):
    return HttpResponse("about page hai")


def removepunc(request):
    return HttpResponse('''Remove Punctuations <a href = "/capitilize/">capitilize</a>''')

def capitilize(request):
    return HttpResponse('''capitilize <a href = "/">home</a>''')