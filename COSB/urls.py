from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^hello$','login.views.hello'),
    url(r'^login$','login.views.login'),
    url(r'^getCAPTCHA','login.views.getCAPTCHA'),
    url(r'^regist$','login.views.regist'),
)
