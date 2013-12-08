 # -*- coding: utf-8 -*
import nltk, urllib, re, string
from urllib import urlopen

def get_defintions(words):
	raw = ""
	urls = ["http://babelnet.org/explore.jsp?word=" + word +"&lang=ES" for word in words]
	meanings = {}
	for url in urls:
		raw = urlopen(url).read()
		defintions = []
		defintions += re.findall(r'color: #333333;">.*</a>', raw)
		defintions = [d[17:-4] for d in defintions]
		meanings[url[37:-8]]= defintions
	return meanings

print get_defintions(["tener", "amigo"])