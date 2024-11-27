from django import forms

class CreateNewTask(forms.Form):
  title = forms.CharField(label='Task Title', max_length=100)
  description = forms.CharField(label='Task Description', widget=forms.Textarea)
  