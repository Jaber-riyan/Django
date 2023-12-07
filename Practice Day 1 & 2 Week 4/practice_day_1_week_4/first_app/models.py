from django.db import models

# Create your models here.
class ModelExample(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=200)
    Choice = {
        ('1','1'),
        ('2','2'),
        ('3','3'),
    }
    rating = models.CharField(max_length=10,choices=Choice)
