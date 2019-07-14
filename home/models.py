from django.db import models

# Create your models here.
class Guides(models.Model):
	name = models.CharField(max_length = 40)
	experience = models.CharField(max_length = 100)
	area = models.CharField(max_length = 100)
	contact = models.CharField(max_length = 100)
	album_logo = models.FileField()
	is_favorite = models.BooleanField(default=False)

	 