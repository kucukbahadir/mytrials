from django.db import models
from datetime import datetime

# Create your models here.

class Zakgeld(models.Model):
    person  = models.CharField(max_length=200)
    task    = models.TextField()
    amount  = models.TextField()   
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.person