from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

def get_default_user():
    try:
        return User.objects.get(id=1)  # Replace with the actual ID of the default user
    except ObjectDoesNotExist:
        return None 

class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    planting_date = models.DateField()
    user = models.ForeignKey('auth.User', related_name='crops', 
                             on_delete=models.CASCADE,
                              default=get_default_user 
                             )
    
    def __str__(self):
        return self.name

class Task(models.Model):
    crop = models.ForeignKey(Crop, related_name='tasks', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
    
class Advice(models.Model):
    title = models.CharField(max_length=200)  # Title of the advice
    content = models.TextField()               # Content of the advice
    image_url = models.URLField(blank=True, null=True)  # URL for an image
    video_url = models.URLField(blank=True, null=True)  # URL for a video

    def __str__(self):
        return self.title