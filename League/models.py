# -*- coding: utf-8 -*-

from django.utils.encoding import smart_text
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Article(models.Model):
    champion = models.ForeignKey('Champion')
    data_time = models.DateTimeField()#Время публикации
    title_article = models.CharField(max_length=100)#Заголовок
    title_text = models.TextField(verbose_name='Текст', blank= True, null= True)#Сам текст
    article_likes = models.IntegerField(default= 0)#A ti ne laykay ne laykay

    def _str_(self):
              return smart_text(self.article_title)


class Comments(models.Model):
    class Meta():
        db_table = 'comments'
    comments_text = models.TextField(verbose_name='Add text_comments')
    comments_article = models.ForeignKey(Article)

class Champion(models.Model):
    name = models.CharField(max_length=30)
    face = models.ImageField(upload_to='face',null = True, blank= True)


class Items(models.Model):
     name = models.CharField(max_length=100)
     face = models.ImageField(blank=True,  help_text='150x150px', verbose_name=name)
     face_par = ImageSpecField(source = 'face', processors=[ResizeToFill(100, 50)], format='JPG',options={'quality':60})
     item_text =models.CharField(max_length=1000)