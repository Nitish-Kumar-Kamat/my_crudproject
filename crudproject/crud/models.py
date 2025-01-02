from django.db import models

class Students(models.Model):
	name=models.CharField(max_length=30)
	lname=models.CharField(max_length=30)
	email=models.EmailField(max_length=30)
	age=models.CharField(max_length=30)
	image=models.FileField(upload_to="mymedia/")
