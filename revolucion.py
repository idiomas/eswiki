import nltk, numpy, urllib, string, re
#copyright Spencer Hitchcock and Huda Khayrallah 

revolution = urllib.urlopen('https://es.wikipedia.org/wiki/Revoluci%C3%B3n_mexicana').read()
m = re.search(r'(en\.wikipedia\.org/wiki/[\S^"]+)\"', revolution)
if m:
    print m.group(1)
revolution = nltk.word_tokenize(revolution)
stops = nltk.corpus.stopwords.words('spanish')

tokens = [w.lower().strip(string.punctuation) for w in revolution if w.lower().strip(string.punctuation) not in stops]
tokens = [w for w in tokens if w.isalpha()]

freq = (nltk.FreqDist(tokens)).keys()



