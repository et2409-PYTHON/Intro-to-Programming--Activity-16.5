import urllib2
from xml.etree import ElementTree

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
s = urllib2.urlopen(url)
print s

tree = ElementTree.parse(s)
print tree

root = tree.getroot()
print root

for child in root:
    print "Train #" ,child[3].text
    print "Direction:" ,child[6].text
    print "Message:" ,child[5].text
    print "Longitude:" ,child[1].text
    print "Latitude:" ,child[2].text
    print "----------------------------"
