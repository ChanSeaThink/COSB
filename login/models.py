from django.db import models

# Create your models here.
class userInfo(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 200)
    nickname = models.CharField(max_length = 30)
    createtime = models.DateTimeField()
