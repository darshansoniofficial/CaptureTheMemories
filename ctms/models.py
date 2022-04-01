from django.db import models
from django import forms
from django.utils.timezone import now
# Create your models here.
class photographer(models.Model):
    Name= models.CharField(max_length=50)
    username = models.CharField(max_length=30, unique=True)
    Profile= models.ImageField(upload_to='media/profile_pic')
    Email_ID = models.EmailField(max_length=255, unique=True)
    Mobile_No = models.CharField(max_length=10, unique=True)
    DOB = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Password=forms.CharField(widget=forms.PasswordInput)
    Address=models.TextField()
    Bio=models.TextField(null=True, blank=True)
    Skills=models.TextField(null=True, blank=True)
    Verified=models.BooleanField(null=True, blank=True)
    Instagram=models.CharField(max_length=2048, null=True, blank=True)
    Facebook=models.CharField(max_length=2048, null=True, blank=True)
    Twiter=models.CharField(max_length=2048, null=True, blank=True)
    Youtube=models.CharField( max_length=2048, null=True, blank=True)
    Created_date = models.DateTimeField(default=now, editable=False)
    
    def __str__(self):
            return self.Name 

class categories(models.Model):
    Name = models.CharField(max_length=50)
    AddedBy = models.ForeignKey(photographer, on_delete=models.CASCADE)

    def __str__(self):
            return self.Name

class photos(models.Model):
    id=models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='media/images/')
    image_id=models.CharField(max_length=100,unique=True) 
    category = models.ForeignKey(categories,on_delete=models.CASCADE)
    Description = models.TextField()
    Publish = models.BooleanField(default=0)
    Tags = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    AddedBy = models.ForeignKey(photographer, on_delete=models.CASCADE)
    Date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
            return self.image_id

class BackgroundImage(models.Model):
    Image =  models.ImageField(upload_to='media/backgroungimages/')
    PAGE_CHOICES = (
        ('i', 'index'),
        ('s', 'single'),
        ('a', 'about'),
        ('c', 'contact')
    )
    Page = models.CharField(max_length=1, choices=PAGE_CHOICES)
    desc = models.CharField(max_length=100)

    def __str__(self):
            return self.Page
    

