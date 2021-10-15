from django.contrib import admin
from .models import *

admin.site.register(QuestionCategory)
admin.site.register(QuestionAnswer)
admin.site.register(Question)