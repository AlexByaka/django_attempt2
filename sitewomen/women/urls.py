from . import views
from django.urls import path, include, register_converter
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('category/<int:cat_id>', views.show_category, name='category'),
    path('post/<slug:post_slug>', views.show_post, name='post'),
]
