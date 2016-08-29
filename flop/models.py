from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=20)


class Question(models.Model):
    user = models.ForeignKey(User)
    score = models.IntegerField()
    created_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    selected_answer = models.OneToOneField('Answer', null=True)
    tags = models.ManyToManyField(Tag)
    rated_by = models.ManyToManyField(User)


class Answer(models.Model):
    user = models.ForeignKey(User)
    score = models.IntegerField()
    created_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    question = models.ForeignKey(Question)
    rated_by = models.ManyToManyField(User)


class Comment(models.Model):
    user = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    answer = models.ForeignKey(Answer, null=True)
    question = models.ForeignKey(Question, null=True)
