from django.db import models
from states.models import State
from datetime import datetime

class StateDocument(models.Model):
    filename = models.CharField(max_length=255)
    filepath  =  models.FileField(verbose_name="Upload GIS Map File",upload_to="state_doc_images")
    created = models.DateTimeField(default= datetime.now(), auto_now= False, auto_now_add=True)
    modified = models.DateTimeField(default= datetime.now, auto_now=True, auto_now_add=False)
    state = models.ForeignKey(State)