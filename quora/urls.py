from django.urls import path
from quora.views import QuestionListView, QuestionDetailView

urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list-page'),
    path('<str:slug>/', QuestionDetailView.as_view(), name='question-details-page'),
]
