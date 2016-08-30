from django.conf.urls import url, include
from .views import QuestionDetailView, signin, signout


urlpatterns = [
    url(r'question/(?P<pk>[0-9]+)/$', QuestionDetailView.as_view(), name='question-detail'),
    url(r'^login/', signin, name='signin'),
]
