from django.db import models

# Create your models here.
class Note(models.Model):
	nsubject = models.CharField(max_length=120)
	ntitle = models.CharField(max_length=120)
	ndesc = models.CharField(max_length=200)


