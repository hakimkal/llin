from django.conf.urls import url, patterns
from django.contrib.auth.views import login, logout
from accounts.views  import   RegisterView 
urlpatterns = patterns('',
               
               url(r'^login/$',login,{'template_name':'accounts/login.html'},name='login'),
               url(r'^logout/$',logout,{'next_page':'/'}, name = 'logout'),
               #url(r'^register/$',views.register,name='register'),
               url(r'^register/$',RegisterView.as_view(),name='register'),
               
               )