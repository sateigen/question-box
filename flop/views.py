from django.shortcuts import render
from .models import Question, Answer, Comment, Tag
from django.contrib.auth.models import User
from .serializers import QuestionSerializer, AnswerSerializer, CommentSerializer, TagSerializer
from rest_framework import viewsets


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
