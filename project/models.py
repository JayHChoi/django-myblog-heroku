from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Project(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField(null=True, blank=True)
	init_date = models.DateTimeField()
	body = models.TextField()
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	cover = models.ImageField(null=True, blank=True, upload_to="images/project/", height_field="height_field",
							  width_field="width_field")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('project:detail', args=[str(self.slug)])

	def save(self, *args, **kwargs):
		if not self.id:
			# Newly created object, so set slug
			self.slug = slugify(self.title)
		super(Project, self).save(*args, **kwargs)
