from django.db import models
from django.urls import reverse


class Education(models.Model):
	title = models.CharField(max_length=50)
	category = models.CharField(max_length=50)
	start_date = models.DateField(null=True, blank=True)
	finish_date = models.DateField(null=True, blank=True)
	finished = models.BooleanField()
	institution = models.CharField(max_length=50)
	instructor = models.CharField(max_length=50, null=True, blank=True)
	url_address = models.URLField()

	def __str__(self):
		return self.title
