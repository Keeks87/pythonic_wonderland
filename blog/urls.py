''' blog/urls.py '''

# Imports
from django.urls import path
from . import views

# URL patterns
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
