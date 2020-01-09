from django.urls import path
from events.views import EventListView, EventDetailView, EventCreateView, ParticipantCreateView

urlpatterns = [
    path('', EventListView.as_view(), name='event-list-page'),
    path('newEvent/', EventCreateView.as_view(), name='create-event-page'),
    path('<str:slug>/', EventDetailView.as_view(), name='event-details-page'),
    path('addParticipant/<str:slug>/', ParticipantCreateView.as_view(), name='add-participant'),
]
