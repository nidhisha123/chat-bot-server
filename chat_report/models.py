from django.db import models

class ChatJokesCounts(models.Model):
	joke = models.CharField(max_length=50)
	count = models.IntegerField(default=0)

	def __str__(self):
		return self.joke.title()

class ChatCunsumerJokesCounts(models.Model):
	user = models.CharField(max_length=100)
	joke = models.CharField(max_length=50)
	count = models.IntegerField(default=0)

	def __str__(self):
		return f'{self.user} - {self.joke.title()}'