from django.conf.urls import url
from League import  views
from django.views.generic import View
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
urlpatterns = [
      url(r'^articles/$', views.articles, name='articles'),
      url(r'^articles/get/(?P<article_id>\d+)/$', views.article, name='article'),
      url(r'^index/$', views.index, name='index'),
      url(r'^articles/addlike/(?P<article_id>\d+)/$', views.addlike, name='article'),
      url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment, name='article'),
      url(r'^articles/addArticle/$', views.ArticleCreate.as_view(), name='album-add'),
      url(r'^articles/UpdateArticle/(?P<article_id>\d+)/$', views.ArticleUpdate.as_view(), name='album-update'),
      url(r'^articles/DeleteArticle/(?P<article_id>\d+)/$', views.ArticleDelete.as_view(), name='album-delete'),
      url(r'', views.articles, name='index'),
]
if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
