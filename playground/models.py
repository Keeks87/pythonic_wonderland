''' playground/models.py '''

# Imports
from django.db import models


class Snippet(models.Model):
    """
    A class representing a code snippet, which is composed of:
    - the title of the snippet
    - the code itself
    - a description of the snippet
    """
    title = models.CharField(max_length=100)
    code = models.TextField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
