''' qna/admin.py '''

# Imports
from django.contrib import admin
from .models import Question, Answer

# Register models.
admin.site.register(Question)
admin.site.register(Answer)
