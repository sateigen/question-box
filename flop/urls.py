from django.conf.urls import url
from .views import QuestionDetailView, UserProfileView
from . import views


urlpatterns = [
    url(r'question/(?P<pk>[0-9]+)/$', QuestionDetailView.as_view(),
        name='question-detail'),
    url(r'^login/', views.signin, name='signin'),
    url(r'^logout/', views.signout, name='signout'),
    url(r'^register/', views.register, name='register'),
    url(r'profile/(?P<pk>[0-9]+)/$', UserProfileView.as_view(),
        name='user_profile'),
    url(r'^questions/$', views.all_questions, name='questions'),
    url(r'$', views.index, name='index'),

]
