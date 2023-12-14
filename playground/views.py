''' playground/views.py '''

# Imports
from django.shortcuts import render
from .models import Snippet

def playground(request):
    '''Playground function
    This function returns the playground page.
    It takes a request object as an argument, which contains information about
    the client's browser and what they are asking for.
    It returns a response object with the playground page.
    The request is passed to this function as an argument.
    '''
    snippets = Snippet.objects.all()
    return render(request, 'playground/playground.html', {'snippets': snippets})
