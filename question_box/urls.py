from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from flop import views

router = routers.DefaultRouter()
router.register(r'question', views.QuestionViewSet)
router.register(r'answer', views.AnswerViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'tag', views.TagViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
