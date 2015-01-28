from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cloudapp.views.home', name='home'),
    url(r'^register/', 'cloudapp.views.register', name='register'),
    url(r'^login/', 'cloudapp.views.ulogin', name='login'),
    url(r'^logout/$', 'cloudapp.views.ulogout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
