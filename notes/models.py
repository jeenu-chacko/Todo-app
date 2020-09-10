from django.db import models
from django import forms

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created = models.DateField(auto_now_add=True)
    deadline = models.DateField(help_text = "Use the following format: <em>YYYY-MM-DD</em>.")
    completed = models.BooleanField(default=False)    

    def __str__(self):
        return self.title
        

        
    