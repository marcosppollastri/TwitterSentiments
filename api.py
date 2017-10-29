import tweepy
from textblob import TextBlob

consumerKey = 'j38xtbtbUVXog8mWcdVrGFRwW'
consumerSecret = 'DLR90KOLpx7qoCdqUzLnWLMZ9nOZBQhXJkhDqtwQnE6kZkXkgL'

accessToken = '3396999435-pW4jApUksxHkxapEeFj6jfDwg3beVTzfI0WxqeH'
accessTokenSecret = '1OLC1y9GcBreXsdviUUOwh5kjSSyQ1iira4SXNdtfo46G'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

#os.system("x-terminal-emulator -e /bin/bash")

print("----Analizador de sentimientos----\n")
print("Bienvenido al analizador de sentimientos!")

busqueda = input('\nIngrese una busqueda:\n\n')
publicTweets = api.search(busqueda)

acumulador = 0
contador = 0

for tweet in publicTweets:

    contador = contador + 1
    print(tweet.text)
    analisis = TextBlob(tweet.text)
    print(analisis.sentiment)
    acumulador = acumulador + analisis.sentiment.polarity
    print('\n')

promedio = acumulador/contador
print("El promedio de polaridad es: ")
print(promedio)
if promedio < 0:
    print('\nEl sentimiento acerca del tema es NEGATIVO')
if promedio == 0:
    print('\nEl sentimiento acerca del tema es NEUTRO')
if promedio > 0:
    print('\nEl sentimiento acerca del tema es POSITIVO')
