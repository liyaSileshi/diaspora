from django.urls import path
from quora.views import QuestionListView, QuestionDetailView, QuestionCreateView

urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list-page'),
    path('newQuestion/', QuestionCreateView.as_view(), name='create-question-page'),
    path('<str:slug>/', QuestionDetailView.as_view(), name='question-details-page'),
]
