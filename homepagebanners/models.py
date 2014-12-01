from django.db import models
from django.contrib.auth import get_user_model


    
    
class Homepagebanner(models.Model):
    null  = "null"
    image = models.ImageField(upload_to="home_slides")
    caption = models.CharField(max_length=255, blank= True, null = True, default=null)
    brief = models.TextField(blank=True, null=True,default=null)
    user = models.ForeignKey(get_user_model())