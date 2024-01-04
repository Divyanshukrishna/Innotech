from django.db import models

# Create your models here.

class data(models.Model):
    username=models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    
    
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='image/')