import requests
from textblob import TextBlob
import urllib.request, json
from django.http import JsonResponse
from django.http import HttpResponse
import json
import nltk
import pickle
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from nltk.classify.scikitlearn import SklearnClassifier
#from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import os
#nltk.download("punkt")
def load_classifiers(file_names):
    classifiers = []
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(cwd)
    for file in file_names:
        classifier_f = open(cwd+"/api/"+file, "rb")
        classifiers.append(pickle.load(classifier_f))

    classifier_f.close
    return classifiers
#classifiers=load_classifiers(["clf1.pickle","clf2.pickle","clf3.pickle"])
def create_features1(words):
    features = {word:True for word in words
                if word not in stopwords.words("english")}
    return features

def textblob_classify(headline):
    threshold = 0
    polarity = TextBlob(headline).sentiment.polarity
    if polarity >= threshold:
        #positive
        return "pos"
    else:
        #negative
        return "neg"

def vader_classify(headline):
    threshold = 0.5
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(headline)
    if vs["compound"] > -threshold:
        return "pos"
    else:
        return "neg"

def most_common(votes):
    pos_count =0
    neg_count=0
    for vote in votes:
        if vote=="pos":
            pos_count+=1
        else:
            neg_count+=1
    if pos_count >= neg_count:
        return "positive"
    else:
        return "negative"

def classify(headline):
    classifiers = load_classifiers(["clf1.pickle","clf2.pickle","clf3.pickle"])
    features = create_features1(word_tokenize(headline))
    votes =[]
    votes.append(textblob_classify(headline))
    votes.append(vader_classify(headline))
    for cl in classifiers:
        votes.append(cl.classify(features))
    return most_common(votes)

API_KEY  = "318d913237d64b00b18eefa946b5ecbe"
LINK = "https://newsapi.org/v2/everything?q="

def get_headlines(query):
    query = '+'.join(query.split('_'))
    link_api = LINK + query + "&language=en&sortBy=popularity&apiKey=" + API_KEY
    with urllib.request.urlopen(link_api) as url:
        data = json.loads(url.read().decode())
        headlines = {"positive":[], "negative":[]}
        for dic in data['articles'][:20]:
            result = classify(dic['title'])
            headlines[result].append({'url':dic['url'], 'title':dic['title']})
        ret = json.dumps(headlines)
        return JsonResponse(json.loads(ret), safe=False)



def home(request, topic):
    #test('rahul')
    return get_headlines(topic)
    #return render(request, 'index.html')
