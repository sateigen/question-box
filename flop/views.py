from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer, Comment, Tag
from django.contrib.auth.models import User
from .serializers import QuestionSerializer, AnswerSerializer, CommentSerializer, TagSerializer
from rest_framework import viewsets


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'flop/question.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        return context


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


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, prefix='user')
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            return HttpResponseRedirect('/')
    else:
        user_form = UserCreationForm(prefix='user')
    context = {'userform': user_form}
    return render(request, 'flop/register.html', context)


def signin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            message = "Invalid login credentials"
    return render(request, 'flop/login.html', context={'message': message})


def signout(request):
    if request.POST:
        return logout(request, request.POST["logout"])
    else:
        logout(request)
        return render(request, 'flop/logout.html')
