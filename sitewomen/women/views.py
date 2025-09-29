from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponse, HttpResponseNotFound
from women.models import Women, Category, TagPost

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    posts = Women.objects.filter(is_published=1)

    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'women/about.html', context=data)


def addpage(request):
    return HttpResponse(f'Добавление страницы')


def contact(request):
    return HttpResponse(f'КОТО Контакты')


def login(request):
    return HttpResponse(f'Войти')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1
    }

    return render(request, 'women/post.html', data)

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.objects.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk
    }
    return render(request, 'women/index.html', context=data)

def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED)

    data = {
        'title': f'Тэг {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None
    }
    return render(request, 'women/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не не найдена</h1>')





