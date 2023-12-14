''' tutorials/urls.py '''

# Imports
from django.urls import path
from . import views

# URL Patterns
urlpatterns = [
    path('', views.tutorial_list, name='tutorial_list'),
    path('<int:pk>/', views.tutorial_detail, name='tutorial_detail'),
]
