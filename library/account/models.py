from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	currentJoboption = [
    ("S","Student"),("E","Employee"),("T","Teaching")
	]
	currentJob = models.CharField(max_length=1, choices=currentJoboption)
	currentcollegeoption = [
    ("1","الكلية التقنية الهندسية -الموصل"),
    ("2","الكلية التقنية الهندسية - كركوك"),
    ("3","الكلية التقنية الادارية"),
	("4","الكلية التقنية الزراعية"),
	("5","المعهد التقني - الموصل "),
	("6","المعهد التقني - نينوى "),
	("7","المعهد التقني - كركوك "),
	("8","المعهد التقني - الدور "),
	("9","المعهد التقني - الحويجة "),
	]
	currentcollege = models.CharField(max_length=1,choices=currentcollegeoption)

	
	def __str__(self):
		return  (self.user.username)
