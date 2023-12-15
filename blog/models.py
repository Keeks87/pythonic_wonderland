'''blog/models.py'''

# Imports
from django.db import models
from django.utils import timezone


class Post(models.Model):
    '''
    Post class
    
    Attributes:
        Title of the post
        Content of the post
        Date the post was created
        Date the post was published
        Methods:
            publish: Publish the post
            __str__: Return the title of the post
    '''
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        '''
        Publish the post
        '''
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
