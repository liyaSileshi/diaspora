from django import forms
from quora.models import Question, Answer
from django.forms import ModelForm, TextInput

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
                'quest'
            ]
        widgets = {
            'quest': TextInput(attrs={'class' : 'input', 'name':'q', 'placeholder' : 'Book Name'}),
        }

class AnswerForm(forms.ModelForm):
    """ Render and process a form based on the Answer model. """
    class Meta:
        model = Answer
        fields = [
                'description'
            ]