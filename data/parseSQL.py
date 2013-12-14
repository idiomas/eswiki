# This Python file uses the following encoding: utf-8
#copyright Spencer Hitchcock and Huda Khayrallah 
import csv, re

test = "(702197,'en','Extended Play (Ladytron EP)'),(540923,'en','Extended SMTP'), (271086,'ca','Àtic (arquitectura)"
text = open('eswiki-latest-langlinks.sql').read()
regex = "([0-9]+),'en','([^']*)'"

matches = re.findall(regex, text, re.S)

with open('artic.csv', 'w') as fp:
    csvwriter = csv.writer(fp, delimiter=',')
    csvwriter.writerow(['spanish', 'english'])

    for item in matches:
        id_num = item[0]
        eslink = 'http://es.wikipedia.org/wiki/index.html?curid=' + id_num

        eng_id = item[1]
        eng_id = eng_id.replace(' ', '_')
        enlink = 'http://en.wikipedia.org/wiki/' + eng_id
        csvwriter.writerow([eslink, enlink])
        print "wrote: \n"  + eslink + "," +  enlink + "\n"
