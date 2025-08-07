from . import views
from django.urls import path, include, register_converter
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('cats/<int:cat_id>', views.catgegories, name='cats_id'),
    path('cats/<slug:cat_slug>', views.catgegories_by_slug, name='cats'),
    path('archive/<year4:year>', views.archive, name='archive'),
]
