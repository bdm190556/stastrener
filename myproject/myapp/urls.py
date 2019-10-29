# НИЖНИЙ

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('programs/', views.programs, name='programs'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
]
