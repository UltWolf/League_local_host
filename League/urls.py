from django.conf.urls import url
from League import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from League.views import *

admin.autodiscover()
urlpatterns = [
      url(r'^articles/$', views.articles),
      url(r'^articles/get/(?P<article_id>\d+)/$', article, name='article'),
      url(r'^index/$', views.index, name='index'),
      url(r'^articles/addlike/(?P<article_id>\d+)/$', views.addlike, name='article'),
      url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment, name='article'),
      url(r'^articles/addArticle/$', views.addarticle, name='album-add'),
      url(r'^articles/UpdateArticle/(?P<article_id>\d+)/$', views.ArticleUpdate.as_view(), name='album-update'),
      url(r'^articles/DeleteArticle/(?P<article_id>\d+)/$', views.ArticleDelete.as_view(), name='album-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

