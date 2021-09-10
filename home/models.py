from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
# hello errors 

class topic(models.Model):
  title=models.CharField(max_length=100)
  short_title=models.CharField(max_length=50,null=True,blank=True)
  slug=models.URLField(max_length=200,null=True,blank=True)
  img= models.URLField(max_length=200,null=True,blank=True)
  icon=models.CharField(max_length=50,null=True,blank=True)
  problems_count = models.IntegerField(default=0,blank=False)
  STATUS = (
    (True, 'Yes'),
    (False, 'No')
  )
  active = models.BooleanField(choices=STATUS,default=False, blank=False)
  last_modified_data = models.DateField(auto_now=True)
  last_modified_time = models.DateTimeField(auto_now=True)

