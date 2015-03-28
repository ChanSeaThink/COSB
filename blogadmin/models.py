# -*- coding: utf8 -*-
from django.db import models

# Create your models here.
class blogArticle(models.Model):
    '''
    此类用于描述存储文章的数据表。

    createtime:文章创建时间。
    blogtitle:文章标题。
    blogcontent:文章内容。
    readtimes:阅读次数。
    commenttimes:评论次数。
    fatherclass:父类名字。
    childclass:子类名字。
    fontnum:字数。
    fatherclassid:父类ID，指向父类表fatherClass的外键。
    childclassid:子类ID，指向子类表childClass的外键。
    '''
    createtime = models.DateTimeField()
    blogtitle = models.CharField(max_length = 60)
    blogcontent = models.TextField()
    readtimes = models.IntegerField()
    commenttimes = models.IntegerField(default = 0)
    fatherclass = models.CharField(max_length = 20, blank = True, null = True)
    childclass = models.CharField(max_length = 20, blank = True, null = True)
    fontnum = models.IntegerField()
    fatherclassid = models.ForeignKey('fatherClass')
    childclassid = models.ForeignKey('childClass')

class blogComment(models.Model):
    '''
    此类用于描述存储评论的数据表。

    nickname:昵称。
    email:评论者邮箱。
    comment:评论内容。
    createtime:评论创建时间。
    contentid:评论所属文章id，指向文章表blogArticle的外键。
    '''
    nickname = models.CharField(max_length = 30)
    email = models.EmailField()
    comment = models.TextField()
    createtime = models.DateTimeField()
    contentid = models.ForeignKey('blogArticle')

class fatherClass(models.Model):
    '''
    此类用于描述存储父类的数据表。

    name:父类名。
    contentnum:该父类下的文章数量。
    childnum:该父类下的子类数量。
    '''
    name = models.CharField(max_length = 20)
    contentnum = models.IntegerField()
    childnum = models.IntegerField()
    
class childClass(models.Model):
    '''
    此类用于描述存储子类的数据表。

    name:子类名。
    contentnum:该子类下的文章数量。
    fatherclass:该子类的父类名。
    fatherclassid:父类ID，指向父类fatherClass的外键。
    '''
    name = models.CharField(max_length = 20)
    contentnum = models.IntegerField()
    fatherclass = models.CharField(max_length = 20)
    fatherclassid = models.ForeignKey('fatherClass')
