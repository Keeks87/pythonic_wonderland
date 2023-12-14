'''portfolio/urls.py'''

# Imports
from django.urls import path
from . import views

# URLs patterns
urlpatterns = [
    path('', views.portfolio, name='portfolio'),
]
