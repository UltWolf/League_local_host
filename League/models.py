# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import smart_text
from django.db import models


class Article(models.Model):
    champion = models.CharField(max_length=20) #БД для чемпионов
    author = models.CharField(max_length=20)#Автор гайда
    data_time = models.DateTimeField()#Время публикации
    title_article = models.CharField(max_length=100)#Заголовок
    title_text = models.TextField(verbose_name='Текст', blank= True, null= True)#Сам текст
    article_likes = models.IntegerField(default = 0)#A ti ne laykay ne laykay
    champion_name  =  models.ForeignKey('Champion')
    def _str_(self):
              return smart_text(self.article_title)


class Comments(models.Model):
    comments_title = models.ForeignKey(Article)
    comments_text = models.TextField(verbose_name='Add text_comments')

class Champion(models.Model):
    name = models.CharField(max_length=30)
    face = models.FileField(blank=True)


class Items(models.Model):
     name = models.CharField(max_length=100)
     face = models.ImageField(blank=True, upload_to='media', help_text='150x150px', verbose_name=name)
     item_text =models.CharField(max_length=1000)