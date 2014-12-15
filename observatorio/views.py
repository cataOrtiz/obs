from observatorio.models import tipo
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
	html = 'index.html'
	return render_to_response(html)
    #return HttpResponse("Hello, world")

def consulta(request):
	elTipo = tipo.objects.all()
	return render_to_response('consultas.html',{'tipo':elTipo})