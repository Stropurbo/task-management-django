from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome to my task management project")

def show_task(request):
    return HttpResponse("This is show task page. ")