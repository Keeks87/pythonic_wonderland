''' qna/models.py '''

# Imports
from django.db import models
from django.utils import timezone

class Question(models.Model):
    """A question on the Q&A site.
    Attributes:
        title: The title of the question.
        text: The text of the question.
        code_snippet: An optional code snippet related to the question.
        created_date: The date the question was created.
    """
    title = models.CharField(max_length=200)
    text = models.TextField()
    code_snippet = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Answer(models.Model):
    """An answer to a question on the Q&A site.
    Attributes:
        question: The question the answer is for.
        text: The text of the answer.
        code_snippet: An optional code snippet related to the answer.
        created_date: The date the answer was created.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    code_snippet = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Answer to {self.question.title}"
