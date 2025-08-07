from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def catgegories(request):
    return HttpResponse('КОТИКИ ДЕЛАЮТ КУСЬ')

