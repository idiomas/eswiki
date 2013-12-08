 # -*- coding: utf-8 -*
import nltk, urllib, re, string, process
from urllib import urlopen

print(process.freq)

def get_defintions(words):
    print "getdef"
    raw = ""
    urls = ["http://babelnet.org/explore.jsp?word=" + word +"&lang=ES" for word in words]
    print "urls: "
    print urls
    meanings = {}
    for url in urls:
        print "looping through words"
        raw = urlopen(url).read()
        defintions = []
        defintions += re.findall(r'color: #333333;">.*</a>', raw)
        defintions = [d[17:-4] for d in defintions]
        meanings[url[37:-8]]= defintions
    return meanings

dict = get_defintions(process.freq) 

for w in dict:
    print w + ": "
    entries = len(dict[w])
    if entries >= 3:
        for d in range(0,2):
             print "    " + dict[w][d]
    elif entries > 0:
        for d in dict[w]:
            print "    " + d
    print ""


