from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class Topic(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title
    
class Reciepe(models.Model):

    CHOICES = (
        ('V', 'Veg'),
        ('NV', 'Non-Veg')
    )

    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    image = models.ImageField(upload_to='ReciepeImages')
    Description = models.TextField()
    foodtype : models.CharField(max_length=200,choices=CHOICES)
    ingridients = models.TextField()
    directions = models.TextField()
    Servings = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    calories = models.CharField(max_length=5)
    fat = models.CharField(max_length=5)
    carbs = models.CharField(max_length=5)
    protein = models.CharField(max_length=5)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    created_by = models.ForeignKey(to=User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
     
