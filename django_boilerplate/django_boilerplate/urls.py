from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_boilerplate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'', TemplateView.as_view(**{'template_name': 'index.html'}), name='index'),
)
