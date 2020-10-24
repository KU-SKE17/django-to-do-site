from django.db import models
from django.core.validators import MinLengthValidator

class Todo(models.Model):
	"""Todo is a task with a description and flag to indicate if it is done"""
	# Require the description to be at least 3 chars
	description = models.CharField('Description', max_length=80, blank=False,
					validators=[MinLengthValidator(3)] )
	done = models.BooleanField('Done?', default=False, blank=True)

	def __str__(self):
		return self.description
