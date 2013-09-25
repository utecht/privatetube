from django.db import models
from django.forms import ModelForm
from django.contrib import admin

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hidden = models.CharField(max_length=5, unique=True)
    vid = models.FileField(upload_to='videos')

admin.site.register(Video)

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'vid']
