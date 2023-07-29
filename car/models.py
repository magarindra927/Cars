from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=50, unique=True)

class Cars(models.Model):
    company=models.ForeignKey(Company, on_delete=models.PROTECT)
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50, unique=True)
    photo=models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    content=RichTextField()    
