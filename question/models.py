from django.db import models

class QuestionCategory(models.Model):
    name                = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    name                = models.CharField(max_length=50, null=True, blank=True)
    correct_answer      = models.CharField(max_length=10, null=True, blank=True)
    question_category   = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class QuestionAnswer(models.Model):
    name                = models.CharField(max_length=50, null=True, blank=True)
    key                 = models.CharField(max_length=10, null=True, blank=True)
    question_answer     = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + self.key
