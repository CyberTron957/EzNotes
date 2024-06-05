from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    content= models.TextField()
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:50]
    
