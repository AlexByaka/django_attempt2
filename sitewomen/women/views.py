from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponse, HttpResponseNotFound
from women.models import Women, Category, TagPost, UploadFiles
from .forms import AddPostForm, UploadFileForm
from django.views import View
from django.views.generic import TemplateView, ListView

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    posts = Women.objects.filter(is_published=1).select_related("cat")

    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0
    }
    return render(request, 'women/index.html', context=data)

class WomenHome(ListView):
    # model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    extra_context = {
        'title': 'Главная страница',
        'menu': menu,
        'cat_selected': 0
    }

    def get_queryset(self):
        return Women.published.select_related("cat")


# import uuid
# def handle_uploaded_file(f):
#     name = f'{str(uuid.uuid1())}_{f.name}'
#     with open(f"uploads/{name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    data = {
        'title': 'О сайте',
        'menu': menu,
        'form': form
    }
    return render(request, 'women/about.html', context=data)


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    data = {
        'menu': menu,
        'title': 'Добавление страницы',
        'form': form
    }
    return render(request, 'women/addpage.html', context=data)


class AddPage(View):
    def get(self, request):
        form = AddPostForm()
        data = {
            'menu': menu,
            'title': 'Добавление страницы',
            'form': form
        }
        return render(request, 'women/addpage.html', context=data)

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        data = {
            'menu': menu,
            'title': 'Добавление страницы',
            'form': form
        }
        return render(request, 'women/addpage.html', context=data)


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
    posts = Women.objects.filter(cat_id=category.pk).select_related("cat")
    data = {
        'title': f'Рубрика {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk
    }
    return render(request, 'women/index.html', context=data)

class WomenCategory(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False
    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related("cat")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Категория' + cat.name
        context['menu'] = menu
        context['cat_selected'] = cat.pk
        return context

def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related("cat")

    data = {
        'title': f'Тэг {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None
    }
    return render(request, 'women/index.html', context=data)

class WomenTagList(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related("cat")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Тэг {get_object_or_404(TagPost, slug=self.kwargs['tag_slug']).tag}"
        context['menu'] = menu
        context['cat_selected'] = None
        return context

def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не не найдена</h1>')
