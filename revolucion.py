import nltk, numpy, matplotlib, urllib, string

revolution = nltk.word_tokenize(urllib.urlopen('https://es.wikipedia.org/wiki/Revoluci%C3%B3n_mexicana').read())
stops = nltk.corpus.stopwords.words('spanish')

tokens = [w.lower().strip(string.punctuation) for w in revolution if w.lower().strip(string.punctuation) not in stops]
tokens = [w for w in tokens if w.isalpha()]

freq = (nltk.FreqDist(tokens)).keys()

print(freq[:400])


