# НИЖНИЙ

from django.urls import path
from . import views
urlpatterns = [
    #path('home/', views.home, name='home'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>', views.topic, name='topic'),
]
