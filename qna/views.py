''' qna/views.py '''

# Imports
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

def qna_list(request):
    '''
    View function for the Q&A list page.
    Args:
        request: An HttpRequest object.
    Returns:
        A rendered HttpResponse object.
    '''
    questions = Question.objects.all().order_by('-created_date')
    return render(request, 'qna/qna_list.html', {'questions': questions})

def qna_detail(request, pk):
    '''
    View function for the Q&A detail page.
    Args:
        request: An HttpRequest object.
        pk: The primary key of the question.
    Returns:
        A rendered HttpResponse object.
    '''
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('qna_detail', pk=question.pk)
    else:
        form = AnswerForm()
    return render(request, 'qna/qna_detail.html', {'question': question, 'form': form})
