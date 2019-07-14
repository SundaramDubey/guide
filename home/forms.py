from django import forms
from .models import Guides

class RegisterForm(forms.ModelForm):
	class Meta:
		model = Guides
		fields=[
				'name',
				
				'experience',
				'area',
				'contact',
		]
		 