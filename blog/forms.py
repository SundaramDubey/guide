from django import forms
from .models import Article

class ModelArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields=[
				'article_name',
				'author',
				'area',
				'content'
		]