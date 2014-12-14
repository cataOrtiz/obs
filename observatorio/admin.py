from django.contrib import admin
from observatorio.models import ciudad
from observatorio.models import comida
from observatorio.models import comida_local
from observatorio.models import comida_tweet
from observatorio.models import hashtag
from observatorio.models import local
from observatorio.models import pais
from observatorio.models import tipo
from observatorio.models import tweet
from observatorio.models import tweet_hashtag
from observatorio.models import twitero

admin.site.register(ciudad)
admin.site.register(comida)
admin.site.register(comida_local)
admin.site.register(comida_tweet)
admin.site.register(hashtag)
admin.site.register(local)
admin.site.register(pais)
admin.site.register(tipo)
admin.site.register(tweet)
admin.site.register(tweet_hashtag)
admin.site.register(twitero)

