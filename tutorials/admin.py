''' tutorials/admin.py '''

# Imports
from django.contrib import admin
from .models import Tutorial, Section

# Register models.
admin.site.register(Tutorial)
admin.site.register(Section)
