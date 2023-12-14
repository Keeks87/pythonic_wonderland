''' playground/urls.py '''

# Imports
from django.urls import path
from . import views

# URL patterns
urlpatterns = [
    path('', views.playground, name='playground'),
]
