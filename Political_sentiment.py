###HTML PARSING#####################
### Thankyou NewsAPI and BeautifulSoup
### CNN API Broken, Fox News no API


import requests
from bs4 import BeautifulSoup
import urllib2
import pickle

#NewsAPI
###CNN###
cnn_news=requests.get('https://newsapi.org/v2/everything?sources=cnn&apiKey=966bdbfa95f749f1b7f2b21f30b7499a')
cnn_json = cnn_news.json()
cnn_articles = cnn_json['articles']
cnn_url_list = []
for x in cnn_articles:
	cnn_url_list.append(x['url'])

democrat = []
for url in cnn_url_list:
#html reader
	try:
		html_doc = urllib2.urlopen(url).read()
	except urllib2.HTTPError:
		pass
	soup = BeautifulSoup(html_doc, 'html.parser')
	body = soup.find_all('div', {'class':'zn-body__paragraph'})
	one_list = []
	for containers in body:
		one_list.append(containers.get_text().encode('ascii', 'ignore'))
	one_string= ''.join(one_list)
	democrat.append(one_string)

###FOX###
fox_news = requests.get('https://newsapi.org/v2/everything?sources=fox-news&apiKey=966bdbfa95f749f1b7f2b21f30b7499a')
fox_json = fox_news.json()
fox_articles = fox_json['articles']
fox_url_list = []
for x in fox_articles:
	fox_url_list.append(x['url'])

republican = []
for url in fox_url_list:
	try:
		html_doc = urllib2.urlopen(url).read()
	except urllib2.HTTPError:
		pass
	soup = BeautifulSoup(html_doc, 'html.parser')
	body = soup.find_all('p')
	body = body[1:-1]
	one_list = []
	for containers in body:
		one_list.append(containers.get_text().encode('ascii', 'ignore'))
	one_string= ''.join(one_list)
	republican.append(one_string)
  
  
  ####Classification#################
  
  import nltk
from nltk import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
import random

class VoteClassifier(ClassifierI):
	def __init__(self, *classifiers):
		self._classifiers = classifiers
	def classify(self, features):
		votes = []
		for c in self._classifiers:
			v = c.classify(features)
			votes.append(v)
		return mode(votes)
	def confidence(self, features):
		votes = []
		for c in self._classifiers:
			v=c.classify(features)
			votes.append(v)
		choice_votes = votes.count(mode(votes))
		conf = choice_votes / len(votes)
		return conf

		
def find_features(document):
	words = word_tokenize(document)
	words_lower = [word.lower() for word in words]
	features = {}
	for w in word_features:
		features[w] = (w in words_lower)
	return features

####CNN 
#democrat = []
news_urls = open("cnn_articles.pickle", "rb")
democrat = pickle.load(news_urls)
news_urls.close()
####FOX
#republican = []
news_urls = open("fox_articles.pickle", "rb")
republican = pickle.load(news_urls)
news_urls.close()


documents = []

for articles in democrat:
	documents.append((articles, 'dem'))
	
for articles in republican:
	documents.append((articles, 'rep'))
	
all_words = []
democrat_words = word_tokenize(''.join(democrat))
republican_words = word_tokenize(''.join(republican))

for word in democrat_words:
	all_words.append(word.lower())

for word in republican_words:
	all_words.append(word.lower())
	
all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:4000]

featuresets = [(find_features(article), category) for (article, category) in documents]
random.shuffle(featuresets)

####Train/Test
training_set = featuresets[:int(len(featuresets)*0.9)]
testing_set = featuresets[int(len(featuresets)*0.9):]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original NBA accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)

classifier.show_most_informative_features(50)

cnn_document = open("cnn_articles.pickle", "wb")
pickle.dump(democrat, cnn_document)
cnn_document.close()

fox_document = open("fox_articles.pickle", "wb")
pickle.dump(republican, fox_document)
fox_document.close()


#######
