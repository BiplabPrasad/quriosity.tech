from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
# hello errors 

class topic(models.Model):
  title=models.CharField(unique=True,max_length=100,null=False,blank=False)
  short_title=models.CharField(unique=True,max_length=50,null=True,blank=True)
  priority = models.IntegerField(unique=True,null=False,blank=False)
  slug=models.CharField(unique=True,max_length=200,null=True,blank=True)
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
  def __str__(self):
    template = 'ID - {0.id} ---> {0.title}({0.problems_count}) ---> ACTIVE - {0.active}'
    return template.format(self)


