''' qna/models.py '''

# Imports
from django.db import models
from django.utils import timezone

class Question(models.Model):
    """A question on the Q&A site.
    Attributes:
        The title of the question.
        The text of the question.
        The date the question was created.
    """
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Answer(models.Model):
    """An answer to a question on the Q&A site.
    Attributes:
        The question the answer is for.
        The text of the answer.
        The date the answer was created.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Answer to {self.question.title}"
