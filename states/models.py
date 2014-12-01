from django.db import models
from image_cropping import ImageRatioField
from datetime import datetime

class State(models.Model):
    maps = models.ImageField(upload_to='maps')
    thumb = ImageRatioField('maps', '1200x1200')
    name= models.CharField(max_length=255,unique=True)
    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True,default=datetime.now())
    modified = models.DateTimeField(auto_now=True, auto_now_add=False, default=datetime.now())
    
    def __unicode__(self):
        return self.name
    #code

