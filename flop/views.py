from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Question, Answer, Comment, Tag
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import QuestionSerializer, AnswerSerializer, CommentSerializer, TagSerializer, UserSerializer
from rest_framework import viewsets
from .forms import UserForm


def index(request):
    return render(request, 'flop/index.html', context={})


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

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Answer.objects.all()
        question = self.request.query_params.get('question', None)
        if question is not None:
            queryset = queryset.filter(question=question)
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = User.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(id=user_id)
        return queryset


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.password = make_password(user_form.cleaned_data['password'])
            user.save()
            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect(reverse('user_profile',
                                                kwargs={'pk': user.id}))
    else:
        user_form = UserForm()
    context = {'userform': user_form}
    return render(request, 'flop/register.html', context)


def signin(request):
    context = {}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('user_profile',
                                                kwargs={'pk': user.id}))
        else:
            context['message'] = "Invalid login credentials"
    return render(request, 'flop/login.html', context)


def signout(request):
    if request.POST:
        return logout(request, request.POST["logout"])
    else:
        logout(request)
        return render(request, 'flop/logout.html')


class UserProfileView(DetailView):
    model = User
    template_name = 'flop/profile.html'
