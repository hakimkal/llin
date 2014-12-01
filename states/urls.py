from django.conf.urls import url, patterns

from states.views import StateListing, MapsStatesListing, StateListFrame, StateDetailView

urlpatterns = patterns('',
                      url(r'^$',StateListing.as_view(), name='listing'),
                      url(r'^maps/$',MapsStatesListing.as_view(), name='maps'),
                      url(r'^stateslist/$', StateListFrame.as_view(), name='states_list'),
                      url(r'^(?P<pk>\d+)/$', StateDetailView.as_view(), name='state'),
                     
                      )