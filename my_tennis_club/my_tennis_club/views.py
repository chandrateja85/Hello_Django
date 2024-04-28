from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Django Learning Journey")

def about(request):
    return HttpResponse("Hi i am going to learn django myself from various sources present on the internet")