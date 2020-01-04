from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from events.models import Event
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

class EventListView(ListView):
    """ Renders a list of all Events. """
    model = Event
    def get(self, request):
        """ GET a list of Events. """
        events = self.get_queryset().all()
        return render(request, 'events/event_list.html', {
          'events': events
        })
