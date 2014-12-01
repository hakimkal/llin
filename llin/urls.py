from django.conf.urls import patterns, include, url

from django.contrib import admin
from states import views as state_view
from django.contrib.auth.views import login,logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'llin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('states.urls')),
    url(r'^maps/$',state_view.MapsStatesListing.as_view()),
    url(r'^stateslist/$', state_view.StateListFrame.as_view()),
                      
    url(r'^states/',include('states.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^login/$',login,{'template_name':'accounts/login.html'},name='login_link'),
      url(r'^logout/$',logout,{'next_page':'/'}, name = 'logout'),
             
    url(r'^accounts/',include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
#for serving media files
from llin import settings  
urlpatterns += patterns(
    'django.views.static',
    (r'media/(?P<path>.*)',
    'serve',
    {'document_root': settings.MEDIA_ROOT}), )