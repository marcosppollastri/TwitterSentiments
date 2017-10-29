import tweepy
from textblob import TextBlob

consumerKey = 'j38xtbtbUVXog8mWcdVrGFRwW'
consumerSecret = 'DLR90KOLpx7qoCdqUzLnWLMZ9nOZBQhXJkhDqtwQnE6kZkXkgL'

accessToken = '3396999435-pW4jApUksxHkxapEeFj6jfDwg3beVTzfI0WxqeH'
accessTokenSecret = '1OLC1y9GcBreXsdviUUOwh5kjSSyQ1iira4SXNdtfo46G'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth, wait_on_rate_limit=True)

#os.system("x-terminal-emulator -e /bin/bash")

print("----Analizador de sentimientos----\n")
print("Bienvenido al analizador de sentimientos!")

busqueda = input('\nIngrese una busqueda:\n\n')

#count = cantidad de tweets
#lang = idioma según ISO 639-1
#showuser = supuestamente es para mostrar los usuarios pero no funca
publicTweets = api.search(busqueda, count=10000, lang='es', show_user='True')

acumulador = 0
contador = 0

for tweet in publicTweets:

    contador = contador + 1

    #print(tweet.text)
    analisis = TextBlob(tweet.text)

    #   para filtrar si se quiere mostrar solo tweets negativos
    #   positivos o lo que se quiera. Modificar el if
    #if analisis.sentiment.polarity < 0:
    if True:
        print(tweet.text)
        print(analisis.sentiment)
        print('\n')

    acumulador = acumulador + analisis.sentiment.polarity


promedio = acumulador/contador
print("El promedio de polaridad es: ")
print(promedio)
if promedio < 0:
    print('\nEl sentimiento acerca del tema es NEGATIVO')
if promedio == 0:
    print('\nEl sentimiento acerca del tema es NEUTRO')
if promedio > 0:
    print('\nEl sentimiento acerca del tema es POSITIVO')
#print('Cantidad de tweet\'s: ' . contador)
