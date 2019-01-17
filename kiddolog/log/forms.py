from django import forms
from .models import Log

class NewLog(forms.ModelForm):
	""" Form for entering new log data """
	class Meta:
		model = Log
		fields = ['kid','date','time','activity','description']
		widgets = {'kid': forms.HiddenInput(), 'date': forms.HiddenInput(),
					'description': forms.Textarea(attrs={'cols': 50, 'rows': 5}),}
		help_texts ={
			'time': '<br>Time of item in 24 hour format<br>(Default value current time)',
			'activity': None,
			'description': None,
		}

class EditLog(NewLog):
	""" Form for editing log data """
	class Meta:
		model = Log
		fields = ['kid','date','time','activity','description']
		help_texts ={
			'time': '<br>Time of item in 24 hour format<br>(Default value current time)',
			'date': '<br>Format of Year-Month-Day (ex. 2019-01-01)',
			'activity': None,
			'description': None,
		}
		widgets = {'description': forms.Textarea(attrs={'cols': 50, 'rows': 5}),}