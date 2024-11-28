from django import forms

class CreateNewProject(forms.Form):
  title = forms.CharField(label='Task Title', max_length=100, widget=forms.TextInput(attrs={'class': 'input'}), required=True)
  description = forms.CharField(label='Task Description', widget=forms.Textarea(
    attrs={'class': 'input'}
  ))
  
class CreateNewTask(forms.Form):
  title = forms.CharField(label='Task Title', max_length=100, widget=forms.TextInput(attrs={'class': 'input'}), required=True)
  description = forms.CharField(label='Task Description', widget=forms.Textarea(
    attrs={'class': 'input'}
  ))
  