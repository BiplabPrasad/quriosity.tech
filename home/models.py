from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
# hello errors 


class topic(models.Model):
  # problem = models.ForeignKey(problem, related_name='topics', null=True, on_delete=models.CASCADE)
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


class problem(models.Model):
  # topic_id = models.IntegerField(null=False,blank=False)
  topic = models.ManyToManyField(topic, verbose_name=_("all topics"))
  title=models.CharField(unique=True,max_length=100,null=False,blank=False)
  short_title=models.CharField(unique=True,max_length=50,null=True,blank=True)
  priority = models.IntegerField(unique=True,null=False,blank=False)
  slug=models.CharField(unique=True,max_length=200,null=True,blank=True)
  problem_url=models.URLField(max_length=200,null=False,blank=False)
  solution_url=models.URLField(max_length=200,null=False,blank=False)
  video_url=models.URLField(max_length=200,null=True,blank=True)
  STATUS = (
    (True, 'Yes'),
    (False, 'No')
  )
  active = models.BooleanField(choices=STATUS,default=False, blank=False)
  last_modified_data = models.DateField(auto_now=True)
  last_modified_time = models.DateTimeField(auto_now=True)
  def __str__(self):
    template = 'ID - {0.id} ---> {0.title} ---> ACTIVE - {0.active}'
    return template.format(self)

class userProblemData(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  problem = models.ForeignKey(problem,on_delete=models.CASCADE)
  STATUS = (
    (True, 'like'),
    (False, 'unlike')
  )
  STATUS2 = (
    (True, 'Yes'),
    (False, 'No')
  )
  like = models.BooleanField(choices=STATUS,null=True, blank=True)
  completed = models.BooleanField(choices=STATUS2,default=False,null=False, blank=False)
  viewed_solution = models.BooleanField(choices=STATUS2,default=False,null=False, blank=False)
  viewed_video = models.BooleanField(choices=STATUS2,default=False,null=False, blank=False)
  shared = models.BooleanField(choices=STATUS2,default=False,null=False, blank=False)
  last_modified_data = models.DateField(auto_now=True)
  last_modified_time = models.DateTimeField(auto_now=True)
  def __str__(self):
    template = 'ID - {0.id} ---> user - {0.user} ---> problem- {0.problem}'
    return template.format(self)

