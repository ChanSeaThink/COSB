from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^hello$','login.views.hello'),
    url(r'^login$','login.views.login'),
    url(r'^getCAPTCHA','login.views.getCAPTCHA'),
    url(r'^regist$','login.views.regist'),
    url(r'^back$','blogadmin.views.back'),
    url(r'^fc$','blogadmin.views.fc'),
    url(r'^cc$','blogadmin.views.cc'),
    url(r'^ba$','blogadmin.views.ba'),
    url(r'^bc$','blogadmin.views.bc'),
)
