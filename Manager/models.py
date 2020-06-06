from django.db import models
from datetime import datetime

class Folder(models.Model):
	folder = models.CharField(max_length=200, default = "misc")
	num_of_entries = models.IntegerField(default=0)

	def __str__(self):
		return self.folder

	class Meta:
		verbose_name_plural = "Folders/Categories"

class Bookmark(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=400)
	folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
	date_of_creation = models.DateTimeField(default=datetime.now())
	notes = models.TextField()

	def __str__(self):
		return self.name
