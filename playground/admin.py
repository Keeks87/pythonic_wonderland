''' playground/admin.py '''

# Imports
from django.contrib import admin
from .models import Snippet

# Register models.
admin.site.register(Snippet)
