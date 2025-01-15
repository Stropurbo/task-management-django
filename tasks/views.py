from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return render(request, "dashboard/manager_dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")

def test(request):
    context = {
        'name' : ['rakib', 'sakib', 'rocky'],
        'age' : 20
    }
    return render(request, 'test.html', context)