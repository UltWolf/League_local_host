# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import smart_text
from django.db import models


class Article(models.Model):
    champion = models.CharField(max_length=20) #БД для чемпионов
    author = models.CharField(max_length=20)#Автор гайда
    meta = models.BooleanField#В мете ли чемпион или нет
    data_time = models.DateTimeField()#Время публикации
    title_article = models.CharField(max_length=100)#Заголовок
    title_text = models.TextField#Сам текст
    article_like = models.IntegerField #A ti ne laykay ne laykay
    def _str_(self):
              return smart_text(self.article_title)


class Comments(models.Model):
    comments_title = models.ForeignKey(Article)
    comments_text = models.TextField(verbose_name='Add text_comments')


