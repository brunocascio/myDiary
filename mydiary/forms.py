from django import forms 
from mydiary.models import Diary

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

#class DiaryForm(forms.Form):
#	title = forms.CharField(max_length=50, required=True)
#	text  = forms.CharField(widget=forms.Textarea, required=True)

class DiaryForm(forms.ModelForm):
	class Meta:
		model = Diary
		exclude = ('author',)