from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from events.models import Event, Participant
from events.forms import EventForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

class EventListView(ListView):
    """ Renders a list of all Events. """
    model = Event
    def get(self, request):
        """ GET a list of Events. """
        events = self.get_queryset().all()
        return render(request, 'events/event_list.html', {
          'events': events
        })

class EventDetailView(DetailView):
    """ Renders a specific event based on it's slug."""
    model = Event
    def get(self, request, slug):
      """ Returns a specific event page by slug. """
      event = self.get_queryset().get(slug__iexact=slug)
      return render(request, 'events/event_detail.html', {
        'event': event
      })

    def post(self, request,slug, *args, **kwargs):
    
        # event = self.objects.get (id = instance.id)
        event= self.get_queryset().get(slug__iexact=slug)
        participants = Participant(event = event)
        participants.save()
        if request.user.is_authenticated():
            participants.user.add(request.user)
            return HttpResponseRedirect(reverse_lazy('event-details-page', args=[event.slug]))

class EventCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': EventForm()}
        return render(request, 'events/new_event.html', context)

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return HttpResponseRedirect(reverse_lazy('event-details-page', args=[event.slug]))
        return render(request, 'events/new_event.html', {'form': form})
    
class ParticipantCreateView(CreateView):
    model = Event
    pass
    # def get(self, request, *args, **kwargs):
    #     context = {'form': EventForm()}
    #     return render(request, 'events/new_event.html', context)

    # use stack overflow as jumpstart example
    # then, if user is logged in, add that user as a participant
    # then that view will be linked to a url and that url will be
    # linked to the join event button! 
    # def post(self, request, *args, **kwargs):
    
    #     event = self.objects.get (id = instance.id)
    #     participants = Participant(event = event)
    #     participants.save()
    #     if request.user.is_authenticated():
    #         participants.user.add(request.user)
    #         return HttpResponseRedirect(reverse_lazy('event-details-page', args=[event.slug]))
        # return render(request, 'events/new_event.html')
    