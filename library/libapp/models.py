from django.db import models
# Create your models here.
import os 

class FileModel(models.Model):
	file=models.FileField(upload_to='allfiles')

	def __str__(self):
		base = os.path.basename(self.file.name)
		return  os.path.splitext(base)[0]


class BooksModel(models.Model):
	call_No=models.CharField(max_length=20)
	title=models.CharField(max_length=100)
	author=models.CharField(max_length=200)
	speciality=models.CharField(max_length=100)
	date=models.CharField(max_length=45,blank=True,default="/")
	publisher_name=models.CharField(max_length=250,blank=True,default="/")
	publisher_place=models.CharField(max_length=250,blank=True,default="/")
	request_number=models.CharField(max_length=250,blank=True,default="/")
	isbn=models.CharField(max_length=100,blank=True,default="/")
	الطبعة=models.CharField(max_length=100,blank=True,default="/")
	active = models.BooleanField(default=True)



	def __str__(self):
		return  (self.title)

class SearchModel(models.Model):
	call_No=models.CharField(max_length=20)
	title=models.CharField(max_length=100)
	author=models.CharField(max_length=200)
	speciality=models.CharField(max_length=100)
	date=models.CharField(max_length=45,blank=True,default="/")
	active = models.BooleanField(default=True)



	def __str__(self):
		return  (self.title)


from django.contrib.auth.models import User
class UserM(User):
    work_group = models.CharField(max_length=20)
    card_num = models.IntegerField()
    def __str__(self):

        return self.user


    

class ThesisModel(models.Model):
	call_No=models.CharField(max_length=20)
	title=models.CharField(max_length=100)
	author=models.CharField(max_length=200)
	speciality=models.CharField(max_length=100)
	اسم_الجامعة=models.CharField(max_length=250,blank=True,default="/")
	اسم_المشرف=models.CharField(max_length=250,blank=True,default="/")
	request_number=models.CharField(max_length=250,blank=True,default="/")
	date=models.CharField(max_length=45,blank=True,default="/")
	active = models.BooleanField(default=True)



	def __str__(self):
		return  (self.title)

class OtherModel(models.Model):
	call_No=models.CharField(max_length=20)
	title=models.CharField(max_length=100)
	author=models.CharField(max_length=200)
	speciality=models.CharField(max_length=100)
	date=models.CharField(max_length=45,blank=True,default="/")
	active = models.BooleanField(default=True)



	def __str__(self):
		return  (self.title)



class FeedBack(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=400)
    body=models.TextField()

    def get_absolute_url(self):
        return '/home'





    def __str__(self):
        return (self.name)




class BestBooks(models.Model):
    book_image=models.ImageField();








































