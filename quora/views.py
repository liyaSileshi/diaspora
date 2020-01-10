from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Answer
from quora.forms import QuestionForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from quora.forms import QuestionForm, AnswerForm


class QuestionCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': QuestionForm()}
        return render(request, 'quora/new_question.html', context)

    def post(self, request, *args, **kwargs):
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(reverse_lazy('question-details-page', args=[question.slug]))
        return render(request, 'quora/new_question.html', {'form': form})
    

class QuestionListView(ListView):
    """ Renders a list of all Questions. """
    model = Question
    def get(self, request):
        """ GET a list of Questions. """
        questions = self.get_queryset().all()
        return render(request, 'quora/question_list.html', {
          'questions': questions
        })


class QuestionDetailView(DetailView):
    """ Renders a specific question based on it's slug."""
    model = Question

    def get(self, request, slug):
        """ Returns a specific question by slug. """
        question = self.get_queryset().get(slug__iexact=slug)
        form = AnswerForm()
        context = {
        'question': question,
        'form' : form
        }
        return render(request, 'quora/question_detail.html', context)   

    def post(self, request, slug):
        question = self.get_queryset().get(slug__iexact=slug)
        form = AnswerForm(request.POST)
        form.instance.author = self.request.user
        if form.is_valid():
        #   print(form.cleaned_data)
          answer = form.save(commit=False)
          answer.question = question
          answer.save()
        #   print(comment)
          return HttpResponseRedirect(reverse('question-details-page',args=(slug,)))


class AnswerDetail(DetailView):
    model = Answer
    context_object_name = "answer"
    template_name = "answer_detail.html"