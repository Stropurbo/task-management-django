from django.shortcuts import render
from django.http import HttpResponse

def user_contact(resquest):
    return HttpResponse("This is users contact page. Call me at +88123456789")

def user_profile(resquest):
    return HttpResponse("Name: Hero alom Home: Bogura Profession: Actor")