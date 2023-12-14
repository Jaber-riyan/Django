from django.db import models
from musician.models import MusicianModel
import datetime

# Create your models here.
class AlbumModel(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(MusicianModel,on_delete = models.CASCADE)
    album_release_date = models.DateTimeField(default=datetime.datetime.today())
    CHOICE = {
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    }
    rating = models.CharField(max_length=100,choices=CHOICE)
    
    
    def __str__(self):
        return self.album_name