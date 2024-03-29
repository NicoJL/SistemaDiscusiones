from django import forms
from .models import Question


class CreateQuestionForm(forms.ModelForm):

	title = forms.CharField(widget = forms.TextInput(attrs = {
					'class': 'form-control',
					'placeholder':'titulo'
		}))

	description = forms.CharField(widget = forms.Textarea(attrs = {
					'class': 'form-control',
					'placeholder':'contenido',
					'rows':4
		}))

	class Meta:
		model = Question