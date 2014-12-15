from django.db import models

class comida_tweet(models.Model):
	id_comida = models.ForeignKey('comida')
	id_tweet = models.ForeignKey('tweet')
	def __unicode__(self):
		return self.id_comida

class ciudad (models.Model):
	nombre = models.CharField(max_length=25)
	id_pais = models.ForeignKey('pais')	
	def __str__(self):
		return self.nombre

class comida (models.Model):
	id_comida = models.IntegerField(default=0)
	nombre = models.CharField(max_length=40)
	id_tipo = models.ForeignKey('tipo')
	def __str__(self):
		return self.nombre

class comida_local(models.Model):
	id_comida = models.ForeignKey('comida')
	id_local = models.ForeignKey('local')
	precio = models.IntegerField(default=0)
	def __unicode__(self):
		return self.id_local

class local(models.Model):
	nombre = models.CharField(max_length=30)
	telefono = models.IntegerField(default=0)
	def __str__(self):
		return self.nombre
class pais(models.Model):
	nombre = models.CharField(max_length=20)
	def __str__(self):
		return self.nombre

class tipo(models.Model):
	tipo = models.CharField(max_length=20)
	def __str__(self):
		return self.tipo

class tweet (models.Model):
	fecha = models.DateField('date published')
	promocion = models.CharField(max_length=50)
	id_ciudad = models.ForeignKey('ciudad')
	id_cuenta = models.ForeignKey('twitero')
	def __unicode__(self):
		return self.id_cuenta

class tweet_hashtag(models.Model):
	id_tweet = models.ForeignKey('tweet')
	id_hashtag = models.ForeignKey('hashtag')
	def __unicode__(self):
		return self.id_hashtag

class twitero(models.Model):
	nombre = models.CharField(max_length=20)
	def __str__(self):
		return self.nombre

class hashtag(models.Model):
	texto = models.CharField(max_length=40)
	def __str__(self):
		return self.texto

