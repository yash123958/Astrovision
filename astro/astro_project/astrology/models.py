from django.db import models
class BirthDetail(models.Model):
     name = models.CharField(max_length=100)
     birth_date=models.DateField()
     birth_time=models.TimeField()

     def __str__(self):
         return self.name


