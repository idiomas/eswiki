 # -*- coding: utf-8 -*
import nltk, urllib, re, string, HTMLParser
from urllib import urlopen

#Return X number of terms from frequency distribution
x = 100

raw = ""

#List of interesting urls of spanish-language wikipedia articles
urls = [
"http://es.wikipedia.org/wiki/Tango",
"http://es.wikipedia.org/wiki/Tango",
"http://es.wikipedia.org/wiki/Tango",
"http://es.wikipedia.org/wiki/Buenos_Aires",
"http://es.wikipedia.org/wiki/Felis_silvestris_catus",
]

#Append all html to raw
for url in urls:
    raw += urllib.urlopen(url).read()

#Get rid of HTML words
raw = nltk.clean_html(raw)
#Split up raw text into tokens
raw= nltk.word_tokenize(raw)
#spanish language stopwords
stops = nltk.corpus.stopwords.words('spanish')

#lowercase words, strip of punctuation, remove stopwords
tokens = [w.lower().strip(string.punctuation)  for w in raw if w.lower().strip(string.punctuation) not in stops and w != ' ']
regex = re.compile("^[0-9]+")
tokens = [w for w in tokens if not regex.match(w)]

freq = (nltk.FreqDist(tokens)).keys()[:x]

for w in freq:
    print(w)
