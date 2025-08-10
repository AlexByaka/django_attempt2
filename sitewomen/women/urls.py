from . import views
from django.urls import path, include, register_converter
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.addpage, name='contact'),
    path('login/', views.addpage, name='login'),
    path('category/<int:cat_id>', views.show_category, name='category'),
    path('post/<int:post_id>', views.show_post, name='post'),
]
