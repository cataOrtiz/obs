from django.db import models

class comida_tweet(models.Model):
	id_comida = models.IntegerField(default=0)
	id_tweet = models.IntegerField(default=0)

class ciudad (models.Model):
	id_ciudad = models.IntegerField(default=0)
	nombre = models.CharField(max_length=6)
	id_pais = models.IntegerField(default=0)

class comida (models.Model):
	id_comida = models.IntegerField(default=0)
	nombre = models.CharField(max_length=40)
	id_tipo = models.IntegerField(default=0)

class comida_local(models.Model):
	id_comida = models.IntegerField(default=0)
	id_local = models.IntegerField(default=0)
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
	id_ciudad = models.IntegerField(default=0)
	id_cuenta = models.IntegerField(default=0)

class tweet_hashtag(models.Model):
	id_tweet = models.IntegerField(default=0)
	id_hashtag = models.IntegerField(default=0)

class twitero(models.Model):
	id_cuenta = models.IntegerField(default=0)
	nombre = models.CharField(max_length=20)

class hashtag(models.Model):
	id_hashtag = models.IntegerField(default=0)
	texto = models.CharField(max_length=40)



