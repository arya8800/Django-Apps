from __future__ import unicode_literals

from django.db import models

class account(models.Model):
	first=models.CharField(max_length=100)
	last=models.CharField(max_length=100)
	email=models.EmailField()
	
	
	def __unicode__(self):
		return "%s" %(self.email)
