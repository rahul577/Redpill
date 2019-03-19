#from django.shortcuts import render
#from rest_framework import viewsets
#from api.models import Blog
#from api.serializer import BlogSerializer
# Create your views here.
#def home(request):
#	if request.GET.get('q'):
#		message = 'You submitted: %r' % request.GET['q']
#		print(message)

#	return render(request, 'index.html')



#class BlogViewSet(viewsets.ModelViewSet):
#	queryset = Blog.objects.all()
#	serializer_class = BlogSerializer
#from textblob import TextBlob
#from bs4 import BeautifulSoup
import requests
#from selenium.webdriver import Firefox
#from selenium.webdriver.firefox.options import Options
from django.http import JsonResponse
import json

"""opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)

threshold = 0
def analyze_headline(headline):
    polarity = TextBlob(headline).sentiment.polarity
    if polarity >= threshold:
        #positive
        return 1
    else:
        #negative
        return -1

headlines = []

def get_page_source(query):
    global headlines
    browser.get(query)
    res = browser.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(res, 'lxml')
    return soup

def scrap_hindustantimes(topic):
    global headlines
    ht_url = "https://www.hindustantimes.com/search?q="
    query = ht_url + topic
    soup = get_page_source(query)
    search_result = soup.find_all('div', class_="media-heading headingfour")
    for div in search_result[:4]:
        link = div.a.get('href')
        heading = div.a.string
        headlines.append([link, heading])

def scrap_indianexpress(topic):
    global headlines
    topic = topic.split()
    topic = "+".join(topic)
    iexpr_url = "https://indianexpress.com/?s="
    query = iexpr_url + topic
    soup = get_page_source(query)
    search_result = soup.find_all('h3', class_="m-article-landing__title")
    for h in search_result[:4]:
        link = h.a.get('href')
        heading = h.a.string
        headlines.append([link, heading])

def scrap_toi(topic):
    global headlines
    topic = topic.split()
    topic = "-".join(topic)
    toi_url = "https://timesofindia.indiatimes.com/topic/"
    query = toi_url + topic
    soup = get_page_source(query)
    search_result = soup.find_all('div', class_="content")
    for div in search_result[:1]:
        span = div.find('span')
        link = div.a.get('href')
        heading = span.string
        heading = heading[1:-1]
        headlines.append([link,heading])


def scrap_cnn(topic):
    global headlines
    topic = topic.split()
    topic = "+".join(topic)
    cnn_url = "https://edition.cnn.com/search/?q="
    query = cnn_url + topic
    soup = get_page_source(query)
    search_result = soup.find('div',class_="cnn-search" )
    search_result = search_result.find_all('div', class_="l-container")[1]
    search_result = search_result.find('div', class_ = "cnn-search__results")
    search_result = search_result.find('div', class_ = "cnn-search__results-list")
    #print(search_result.prettify())
    for h in search_result.find_all('h3', class_="cnn-search__result-headline")[:4]:
        link = h.a.get('href')
        heading = h.a.string
        headlines.append([link,heading])

topic = "india airstrikes pakistan"

def scrapper(topic):
    #scrap_cnn(topic)
    scrap_toi(topic)
    #scrap_indianexpress(topic)
    #scrap_hindustantimes(topic)

    analyzed_headlines = [[h[0],h[1],analyze_headline(h[1])] for h in headlines]
    browser.quit()
    #print(JsonResponse(json.dumps(analyzed_headlines), safe=False))
    return JsonResponse(json.dumps(analyzed_headlines), safe=False)


#analyzed_headlines = scrapper(topic)
#print(*analyzed_headlines, sep='\n')"""

def test(temp):
    l = {'a' : 1, 'b' : 2, 'c' : 3}
    #if temp == 'rahul':
    return JsonResponse(json.dumps(l), safe=False)
    

def home(request):
    temp('rahul')
    return render(request, 'index.html')