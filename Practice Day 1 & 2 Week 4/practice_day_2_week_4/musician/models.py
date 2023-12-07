from django.db import models

# Create your models here.

class MusicianModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=12)
    instrument_type = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
