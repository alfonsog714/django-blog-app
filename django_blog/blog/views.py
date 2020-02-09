from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Blog Home</h1>")


def test(request):
    return HttpResponse("<h1>Testing</h1> <h2>Testing still</h2>")
