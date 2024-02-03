from django.db import models

# Create your models here.
class Student(models.Model):
    stid = models.IntegerField()
    stuname = models.CharField(max_length=20)
    stuemail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length= 70)

    def __str__(self):
        return self.stuname
    
