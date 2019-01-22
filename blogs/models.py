from django.db import models
from django.utils import timezone

# Create your models here.
class blogs(models.Model):
	Title = models.CharField(max_length=200)
	Blog = models.TextField()
	Author = models.CharField(max_length=200)
	Created_date =models.DateTimeField(default=timezone.now)
