from django.db import models
from django.db import models

# Create your models here.
class Art(models.Model):
	title = models.CharField(max_length = 30)
	description = models.TextField()
	area = models.CharField(max_length = 10)
	picture = models.FileField(default = '')

	 
