from django.shortcuts import render
from django.http import HttpResponse


def home(r):
    return HttpResponse('hello world !')