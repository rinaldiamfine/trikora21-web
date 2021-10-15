from django.urls import path, include
from . import views

from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'question-category', views.QuestionCategoryViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'question-answer', views.QuestionAnswerViewSet)

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]