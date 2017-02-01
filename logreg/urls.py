from django.conf.urls import url

from logreg.views import login,logout


urlpatterns = [

    url(r'^login/$',  login, name='article'),
    url(r'^logout/$', logout, name='article'),

]