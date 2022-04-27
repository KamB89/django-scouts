from django.db import models

# Create your models here.
class Scout(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    weight = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null = True, blank = True)
    
    
    def __str__(self):
        return f"My name is {self.name} and I am {self.desc}"