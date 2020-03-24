from django.db import models

# Create your models here.
class Info(models.Model):
    post_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=90)
    image=models.ImageField(upload_to='music/images',default="")
    song=models.FileField(upload_to='music/audio',default="")
    text=models.CharField(max_length=10000)
    lyrics=models.CharField(max_length=1000000,default=0)

def __str__(self):
    return self.name   
