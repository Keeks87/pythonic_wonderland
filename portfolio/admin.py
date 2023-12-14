''' portfolio/admin.py '''

# Imports
from .models import Project
from django.contrib import admin

# Registering Project model in admin portal
admin.site.register(Project)
