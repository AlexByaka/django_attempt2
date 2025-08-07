from django.shortcuts import render, reverse, redirect, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse('Главная страница')


def catgegories(request, cat_id):
    return HttpResponse(f'<h1>КОТИКИ ДЕЛАЮТ КУСЬ</h1><p>{cat_id}</p>')


def catgegories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>ПО слагу {cat_slug}</p>')


def archive(request, year):
    if year > 2025:
        url = reverse('cats', args=['invalid-year'])
        return redirect(url)
    return HttpResponse(f'<h1>Архив</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не не найдена</h1>')
