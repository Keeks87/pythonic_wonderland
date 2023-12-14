''' tutorials/models.py '''

# Imports
from django.db import models

class Tutorial(models.Model):
    """ A tutorial is a self-contained lesson or set of instructions for
    learning a specific topic.
    Attributes:
        The title of the tutorial.
        A brief introduction to the tutorial.
        The content of the tutorial.
        The date and time the tutorial was created.
        The date and time the tutorial was last updated.
    """
    title = models.CharField(max_length=200)
    introduction = models.TextField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Section(models.Model):
    """ A section is a subtopic within a tutorial.
    Attributes:
        The tutorial the section belongs to.
        The title of the section.
        The content of the section.
    """
    tutorial = models.ForeignKey(Tutorial, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
