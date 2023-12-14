""" pythonic_wonderland/urls.py """

# Imports
from django.contrib import admin
from django.urls import path, include

# URLs patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('playground/', include('playground.urls')),
    path('', include('portfolio.urls')),
    path('qna/', include('qna.urls')),
    path('tutorials/', include('tutorials.urls')),
]
