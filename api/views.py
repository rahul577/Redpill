import requests
from textblob import TextBlob
import urllib.request, json
from django.http import JsonResponse
from django.http import HttpResponse
import json


threshold = 0
def analyze_headline(headline):
 polarity = TextBlob(headline).sentiment.polarity
 if polarity >= threshold:
     #positive
     return 1
 else:
     #negative
     return -1

API_KEY  = "318d913237d64b00b18eefa946b5ecbe"
LINK = "https://newsapi.org/v2/everything?q="
def get_headlines(query):
 query = '+'.join(query.split())
 with urllib.request.urlopen(f"{LINK}{query}&language=en&sortBy=popularity&apiKey={API_KEY}") as url:
     data = json.loads(url.read().decode())
     #print(*[dic['title'] for dic in data['articles'][:20]], sep='\n')
     headlines = [{'url':dic['url'], 'title':dic['title'],
                   'label':analyze_headline(dic['title'])}
                  for dic in data['articles'][:20]]



     ret = json.dumps(headlines[0])
     return JsonResponse(json.loads(ret))

#print(*get_headlines("india pakistan tension"), sep='\n')

#analyzed_headlines = scrapper(topic)
#print(*analyzed_headlines, sep='\n')

"""def test(temp):
    return get_headlines('new zealand terror attack')
    l = {'a' : 1, 'b' : 2, 'c' : 3}
    #if temp == 'rahul':
    return JsonResponse(json.dumps(l), safe=False)"""


def home(request):
    #test('rahul')
    return get_headlines('new zealand terror attack')
    #return render(request, 'index.html')
