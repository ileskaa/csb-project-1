import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# Each model is represented by a class that subclasses django.db.models.Model
# Each class variable represents a database field in the model
# Each field is represented by an instance of a Field class


class Question(models.Model):
    # CharField requies that you give it a max length
    question_text = models.CharField(max_length=200)
    # you can use an optional first positional argument to a Field to designate
    # a human readable name
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # ForeignKey tells Django each choice is related to a single question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
