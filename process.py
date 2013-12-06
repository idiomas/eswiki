 # -*- coding: utf-8 -*
import nltk, urllib, re, string
from urllib import urlopen

raw = ""
urls = [
"http://es.wikipedia.org/wiki/Tango",
"http://es.wikipedia.org/wiki/Tango",
"http://es.wikipedia.org/wiki/Tango",
"http://es.wikipedia.org/wiki/Buenos_Aires",
"http://es.wikipedia.org/wiki/Felis_silvestris_catus",
]

print urls

for url in urls:
    raw += urlopen(url).read()

raw= nltk.word_tokenize(raw)
stops = nltk.corpus.stopwords.words('spanish')

tokens = [w.lower().strip(string.punctuation) for w in raw if w.lower().strip(string.punctuation) not in stops]
tokens = [w for w in tokens if w.isalpha()]

freq = (nltk.FreqDist(tokens)).keys()[:100]

print(freq)



