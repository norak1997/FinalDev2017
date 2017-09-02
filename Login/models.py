from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
#from Game.models import GroupDetails

# Create your models here.

class UserProfile(models.Model):
	types = (('Mess Worker','Mess Worker'),('Student','Student'))
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	typid = models.CharField(max_length = 30,choices = types,default='Student')
	extras = models.IntegerField(max_length = 5,default = 0)
	regno = models.IntegerField(max_length = 6)


	def __str__(self):
		return self.user.first_name