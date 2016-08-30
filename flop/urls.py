from django.conf.urls import url, include
from .views import QuestionDetailView, signin, signout, register, UserProfileView


urlpatterns = [
    url(r'question/(?P<pk>[0-9]+)/$', QuestionDetailView.as_view(), name='question-detail'),
    url(r'^login/', signin, name='signin'),
    url(r'^logout/', signout, name='signout'),
    url(r'^register/', register, name='register'),
    url(r'profile/(?P<pk>[0-9]+)/$', UserProfileView.as_view(), name='user_profile'),
]
