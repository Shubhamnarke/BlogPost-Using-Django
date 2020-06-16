from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	name = models.CharField(blank = False,max_length = 100)
	email = models.EmailField()
	discription = models.TextField(blank = False)
	author = models.CharField(default = "Unknown author",max_length = 100)

	def get_absolute_url(self):
		return reverse("one_post" ,kwargs = {'id':id})