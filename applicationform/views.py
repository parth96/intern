from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'buy.html')

def exam(request):
    return HttpResponse("hello world")