from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(\d+)\+(\d+)$', 'calc.views.suma'),
    url(r'^(\d+)\-(\d+)$', 'calc.views.resta'),
    url(r'^(\d+)\/(\d+)$', 'calc.views.div'),
    url(r'^(\d+)\*(\d+)$', 'calc.views.multi'),
    url(r'.', 'calc.views.error')
)
