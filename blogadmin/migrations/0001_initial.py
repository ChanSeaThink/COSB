# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createtime', models.DateTimeField()),
                ('blogtitle', models.CharField(max_length=60)),
                ('blogcontent', models.TextField()),
                ('readtimes', models.IntegerField()),
                ('fatherclass', models.CharField(max_length=20, null=True, blank=True)),
                ('childclass', models.CharField(max_length=20, null=True, blank=True)),
                ('fontnum', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='blogComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
                ('comment', models.TextField()),
                ('createtime', models.DateTimeField()),
                ('contentid', models.ForeignKey(to='blogadmin.blogArticle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='childClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('contentnum', models.IntegerField()),
                ('fatherclass', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='fatherClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('contentnum', models.IntegerField()),
                ('childnum', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='childclass',
            name='fatherclassid',
            field=models.ForeignKey(to='blogadmin.fatherClass'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogarticle',
            name='childclassid',
            field=models.ForeignKey(to='blogadmin.childClass'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogarticle',
            name='fatherclassid',
            field=models.ForeignKey(to='blogadmin.fatherClass'),
            preserve_default=True,
        ),
    ]
