from django.db import models
# Create your models here.
from django.urls import reverse
class Article(models.Model):
	article_name = models.CharField(max_length =100)
	author = models.CharField(max_length =100)
	area = models.CharField(max_length = 100)
	content = models.TextField()

	def get_absolute_url(self):

			#return f"/products/{self.id}/"  # but it is just a string we have to make it Dynamic ...
			return reverse("article-detail", kwargs={"id":self.id})

