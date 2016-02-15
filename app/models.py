# coding=utf8
# -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models

class Promos(models.Model):
	title = models.CharField(max_length = 100, unique=True)
	short_desc = models.CharField(max_length = 100)
	long_desc = models.CharField(max_length = 1000)
	location = models.CharField(max_length = 100)
	contact = models.CharField(max_length = 12)
	image_url = models.CharField(max_length = 255, unique=True)
	price = models.FloatField(default = 0.00)

	def __str__(self):
		return u'%s_%s' % (self.title, self.location)
	def __unicode__(self):
		return u'%s_%s' % (self.title, self.location)

class Wishes(models.Model):
	#user_fk = models.ForeignKey(User)
	name = models.CharField(max_length = 100, unique=True)
	short_desc = models.CharField(max_length = 100)
	cost = models.FloatField(default = 0.00)
	contact = models.CharField(max_length = 12)
	video_url = models.CharField(max_length = 255, unique=True)
	approved = models.BooleanField(default=True)

	def __str__(self):
		return self.name
	def __unicode__(self):
		return self.name