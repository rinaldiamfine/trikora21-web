from django.shortcuts import render
from .models import *
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view
from .serializers import *
from random import randint

class QuestionCategoryViewSet(viewsets.ModelViewSet):
    queryset =  QuestionCategory.objects.all()
    serializer_class = QuestionCategorySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        if self.request.method == "GET":
            q = self.request.GET.get('q', '')
            if q:
                queryset = queryset.filter(question_category=q)
                length_query = len(queryset)
                random_index = randint(0, length_query - 1)
                random_value = queryset[random_index]
                random_q = queryset.filter(question_category=q, id=random_value.id)
                return random_q
        return queryset
    
class QuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer

    def get_queryset(self):
        queryset = QuestionAnswer.objects.all()
        if self.request.method == "GET":
            q = self.request.GET.get('q', '')
            if q:
                queryset = queryset.filter(question_answer=q)
        return queryset
    