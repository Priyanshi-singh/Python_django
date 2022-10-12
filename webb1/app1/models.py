#from cgitb import text
#from typing_extensions import Required
#from django.db import models
from django.db.models import *

# model #shortcut to create model

class Movies(Model):
    title = CharField(max_length=50)
    year = IntegerField()
    rating = FloatField()



