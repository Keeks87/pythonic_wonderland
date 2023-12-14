''' qna/urls.py '''

# Imports
from django.urls import path
from . import views

# URL patterns
urlpatterns = [
    path('', views.qna_list, name='qna_list'),
    path('question/<int:pk>/', views.qna_detail, name='qna_detail'),
]
