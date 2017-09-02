from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


class Purchase(models.Model):

	regno = models.IntegerField(max_length = 6)
	item = models.CharField(max_length = 30)
	quantity = models.IntegerField(max_length = 3)
	price = models.IntegerField(max_length = 4)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		# t = (item + char(quantity) + char(regno))
		return self.item

class Items(models.Model):
	name = models.CharField(max_length = 30)
	price = models.IntegerField(max_length = 10)

	def __str__(self):
		return self.name


# Create your models here.
