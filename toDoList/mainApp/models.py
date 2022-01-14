from pydoc import describe
from pyexpat import model
from django.db import models

# Create your models here.
class toDoList(models.Model):
    Title = models.CharField(max_length=100, blank=False)

    Describe = models.TextField(blank=True)
    Date = models.DateField(blank=False)
    Completed = models.BooleanField(default=False)

    def ___str___(self):
        return self.Title
