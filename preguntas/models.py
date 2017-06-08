from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


class Question(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	topic = models.CharField(max_length=100)
	question_text = models.CharField(max_length=200)
	imagen=models.ImageField(blank=True,default='',upload_to='pics')
	c1=models.CharField(max_length=200,default='1')
	c2=models.CharField(max_length=200,default='2')
	c3=models.CharField(max_length=200,default='3')
	correct=models.IntegerField(default='1')
	def __str__(self):
		return self.question_text

class Choice(models.Model):
	choice_text = models.CharField(max_length=200)
	correct = models.BooleanField(default=False)
	question = models.ForeignKey(Question, on_delete=models.CASCADE,default=1)
	def __str__(self):
		return self.choice_text
class Jugador(models.Model):
	nick=models.CharField(max_length=100)

class Historico(models.Model):
	aciertos=models.IntegerField()
	fallos=models.IntegerField()
	jugador=models.ForeignKey(Jugador,on_delete=models.CASCADE,default=1)