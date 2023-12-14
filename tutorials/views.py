''' tutorials/views.py '''

# Imports
from django.shortcuts import render, get_object_or_404
from .models import Tutorial

def tutorial_list(request):
    """ A view that returns a list of all the tutorials in the database as an
    HTML response. 
    """
    tutorials = Tutorial.objects.all().order_by('-created_date')
    return render(request, 'tutorials/tutorial_list.html', {'tutorials': tutorials})

def tutorial_detail(request, pk):
    """ A view that returns a single tutorial object based on the tutorial's
    primary key (pk) and renders it to the 'tutorial_detail.html' template.
    Or returns a 404 error if the tutorial is not found.
    """
    tutorial = get_object_or_404(Tutorial, pk=pk)
    return render(request, 'tutorials/tutorial_detail.html', {'tutorial': tutorial})
