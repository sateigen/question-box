from django.conf.urls import url
from .views import QuestionDetailView

urlpatterns = [
    url(r'question/(?P<pk>[0-9]+)/$', QuestionDetailView.as_view(), name='question-detail'),
]
