from django.db import models

from django.contrib.auth.models import User

class Integrante(models.Model):
	user = models.OneToOneField(User)


	def username(self):
		return self.user.username
		
	def __str__(self):
		return self.user.username
