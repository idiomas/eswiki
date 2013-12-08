 # -*- coding: utf-8 -*
import nltk, urllib, re, string
from urllib import urlopen

raw = ""
urls = [
"http://babelnet.org/explore.jsp?word=amigo&lang=ES", "http://babelnet.org/explore.jsp?word=tengo&lang=ES"
]

#print urls
#re.findall(r'>.*</a>', raw)
meanings = {}
for url in urls:
    raw += urlopen(url).read()
    defintions = []
    defintions += re.findall(r'color: #333333;">.*</a>', raw)
    defintions = [d[17:-4] for d in defintions]
    meanings[url[37:-8]]= defintions


print meanings







