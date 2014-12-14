from django.db import models

class comida_tweet(models.Model):
	id_comida = models.ForeignKey('comida')
	id_tweet = models.ForeignKey('tweet')

class ciudad (models.Model):
	id_ciudad = models.IntegerField(default=0)
	nombre = models.CharField(max_length=25)
	id_pais = models.ForeignKey('pais')

class comida (models.Model):
	id_comida = models.IntegerField(default=0)
	nombre = models.CharField(max_length=40)
	id_tipo = models.ForeignKey('tipo')

class comida_local(models.Model):
	id_comida = models.ForeignKey('comida')
	id_local = models.ForeignKey('local')
	precio = models.IntegerField(default=0)


class local(models.Model):
	id_local = models.IntegerField(default=0)
	nombre = models.CharField(max_length=30)
	telefono = models.IntegerField(default=0)

class pais(models.Model):
	id_pais = models.IntegerField(default=0)
	nombre = models.CharField(max_length=20)

class tipo(models.Model):
	tipo = models.CharField(max_length=20)
	id_tipo = models.IntegerField(default=0)

class tweet (models.Model):
	id_tweet = models.IntegerField(default=0)
	fecha = models.DateField('date published')
	promocion = models.CharField(max_length=50)
	id_ciudad = models.ForeignKey('ciudad')
	id_cuenta = models.ForeignKey('twitero')

class tweet_hashtag(models.Model):
	id_tweet = models.ForeignKey('tweet')
	id_hashtag = models.ForeignKey('hashtag')

class twitero(models.Model):
	id_cuenta = models.IntegerField(default=0)
	nombre = models.CharField(max_length=20)

class hashtag(models.Model):
	id_hashtag = models.IntegerField(default=0)
	texto = models.CharField(max_length=40)



