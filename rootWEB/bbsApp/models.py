from django.db import models
# add
from django.utils import timezone

# Create your models here.
class BbsUser(models.Model):
    user_id = models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_id+"\t"+self.user_pwd+"\t"+self.user_name


class Bbs(models.Model):
    # id도 존재하는 것.(기본키로 자동으로 세팅해줘서)
    title   = models.CharField(max_length=500)
    writer  = models.CharField(max_length=100)
    content = models.TextField()
    regdate = models.DateTimeField(default=timezone.now)
    viewcnt = models.IntegerField(default=0)

class Timeline(models.Model):
    # id
    txt = models.CharField(max_length=500)
    writer = models.CharField(max_length=100)
    board_id = models.IntegerField()