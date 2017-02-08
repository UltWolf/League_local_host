from django.conf.urls import url

from logreg.views import login,logout,register


urlpatterns = [

    url(r'^login/$',  login, name='article'),
    url(r'^logout/$', logout, name='article'),
    url(r'^register/$', register),
]