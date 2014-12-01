from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import State
from homepagebanners.models import Homepagebanner
from states_documents.models import StateDocument

class StateListing(ListView):
    model = State
    
    def get_context_data(self,**kwargs):
        context = super(StateListing,self).get_context_data(**kwargs)
        context['slides'] = Homepagebanner.objects.all()
        return context


class StateListFrame(ListView):
    model = State
    template_name = 'states/lists.html'
    queryset = State.objects.order_by("name").all().select_related()
    #paginate_by = 2
        
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(StateListFrame, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the states
        context['state_documents_list'] = StateDocument.objects.all()
        print context
        return context

class MapsStatesListing(ListView):
    model = StateDocument
    template_name = 'states/maps_states.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MapsStatesListing, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the states
        context['state_list'] = State.objects.all()
        return context
    
class StateDetailView(DetailView):
    context_object_name = 'state'
    model = State
    #d = State.StateDocument.objects.all()
    #print d
