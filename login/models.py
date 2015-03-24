# -*- coding: utf8 -*-
from django.db import models

# Create your models here.
class userInfo(models.Model):
    '''
    描述和创建用户信息表

    注册时，前端js将会进行判断，把账户和密码控制在15个字符以内，
    昵称控制在10个字符以内。

    username表示用户名。
    password存储的是密码+创建时间的哈希。
    nickname是昵称。
    cretetime是创建时间。
    '''
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 200)
    nickname = models.CharField(max_length = 30)
    createtime = models.DateTimeField()
    
    #def __unicode__(self):
        #return self.username

    #def __unicode__(self):
        #return '%s %s %s %s' % (self.username, self.password, self.nickname, self.createtime)
