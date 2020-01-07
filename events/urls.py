from django.urls import path
from events.views import EventListView, EventDetailView

urlpatterns = [
    path('', EventListView.as_view(), name='event-list-page'),
    path('<str:slug>/', EventDetailView.as_view(), name='event-details-page'),
]
