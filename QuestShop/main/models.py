from django.db import models
from django.forms import ModelForm

# Create your models here.

class Work(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    main_img = models.ImageField(upload_to="work")
    sub_title = models.CharField(max_length=200)
    content = models.TextField()

class MainImg(models.Model):
    mainImg = models.ImageField(upload_to="main")

class Contact(models.Model):
    company = models.CharField(max_length=20)
    client = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    project = models.CharField(max_length=50)
    detail = models.TextField()



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['company', 'client', 'phone', 'email', 'project', 'detail']