from django.db import models
from django.utils import timezone
# Create your models here.



# class Question(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     question_text =models.CharField(max_length=500)
#     regdate = models.DateTimeField(default=timezone.now)
#
# class Choice(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     question_text=models.ForeignKey(Question,on_delete=models.CASCADE,db_column='question_text')
#     choice_text=models.CharField(max_length=200)
#     votes=models.IntegerField(default=0)

class QuestionTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_text =models.CharField(max_length=500)
    regdate = models.DateTimeField(default=timezone.now)

class ChoiceTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_text=models.ForeignKey(QuestionTbl,on_delete=models.CASCADE,db_column='question_text')
    choice_text=models.CharField(max_length=200)
    vote=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text