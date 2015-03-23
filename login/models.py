# -*- coding: utf8 -*-
from django.db import models

# Create your models here.
class userInfo(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 200)
    nickname = models.CharField(max_length = 30)
    createtime = models.DateTimeField()
    
    #def __unicode__(self):
        #return self.username

    #def __unicode__(self):
        #return '%s %s %s %s' % (self.username, self.password, self.nickname, self.createtime)
