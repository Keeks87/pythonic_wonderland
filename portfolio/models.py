''' portfolio/models.py '''

# Imports
from django.db import models


class Project(models.Model):
    """ 
    A project that a user is working on.
    
    Fields: 
        The title of the project.
        A description of the project.
        A snippet of code from the project.
        A link to the project's GitHub repo.
        A link to the project's live demo.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    code_snippet = models.TextField()
    github_link = models.URLField()
    live_demo_link = models.URLField()

    def __str__(self):
        return self.title
