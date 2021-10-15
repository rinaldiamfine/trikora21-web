from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

class QuestionCategoryViewSet(viewsets.ModelViewSet):
    queryset =  QuestionCategory.objects.all()
    serializer_class = QuestionCategorySerializer
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class QuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    