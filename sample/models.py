from django.db import models

# Create your models here.
class Sample(models.Model):
    

    title1 = models.CharField(max_length=100)   
    description = models.CharField(null=True,max_length=100) 
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    image = models.ImageField(null=True, blank=True, upload_to='sample')

    def __str__(self):
        return self.title1 