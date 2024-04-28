from django.shortcuts import render
from django.http import HttpResponse

def firstApp(request):
    return render(request,'sample.html',{'name':'Kiran'})