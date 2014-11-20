from django.conf.urls import patterns, include, url
from django.contrib   import admin

#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'mydiary.views.login', name="login"),
    url(r'^logout/$', 'mydiary.views.logout', name="logout"),

    url(r'^diaries/$', 'mydiary.views.index', name="diaries"),
    url(r'^diaries/(?P<diary_id>\d+)/$', 'mydiary.views.show', name="diary_detail"),
    url(r'^diaries/(?P<diary_id>\d+)/delete/$', 'mydiary.views.destroy', name="diary_delete"),
    url(r'^diaries/create/$', 'mydiary.views.create', name="diary_create"),
)
