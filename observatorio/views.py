from observatorio.models import comida, tipo, ciudad, pais, twitero, tweet, comida_tweet
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Count


def index(request):
	html = 'index.html'
	return render_to_response(html)
    #return HttpResponse("Hello, world")

def consulta(request):
	elTipo = tipo.objects.all()
	laCiudad = ciudad.objects.all()
	elPais = pais.objects.all()
	return render_to_response('consultas.html',{'tipo':elTipo, 'ciudad':laCiudad, 'pais':elPais})

#la comida mas consumida en ciudad dato1
def respuestas(request, dato1):
	idciudad = ciudad.objects.filter(nombre=dato1)
	idTweet = tweet.objects.filter(id_ciudad__in=idciudad)
	idComida = comida_tweet.objects.filter(id_tweet__in=idTweet)
	result = comida.objects.filter(id_comida__in=idComida)
	return render_to_response('respuestas.html',{'result':result})