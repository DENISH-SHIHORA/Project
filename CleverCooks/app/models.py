from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class Topic(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title

class Reciepe(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    image = models.CharField(max_length=400)
    Description = models.TextField()
    ingridients = models.TextField()
    directions = models.TextField()
    Servings = models.CharField(max_length=5)
    time = models.CharField(max_length=5)
    calories = models.CharField(max_length=5)
    fat = models.CharField(max_length=5)
    carbs = models.CharField(max_length=5)
    protein = models.CharField(max_length=5)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    created_by = models.ForeignKey(to=User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
     
