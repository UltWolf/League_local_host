from django.conf.urls import url
from League import views


urlpatterns = [
      url(r'^articles/all/$', views.articles, name='articles'),
      url(r'^articles/get/(?P<article_id>\d+)/$', views.article, name='article'),
      url(r'^index/$', views.index, name='articles'),
      url(r'^articles/addlike/(?P<article_id>\d+)/$', views.addlike, name='article'),
      url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment, name='article'),
]