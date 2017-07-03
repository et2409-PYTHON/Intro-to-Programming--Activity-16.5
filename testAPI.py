import urllib2
from xml.etree import ElementTree

url = "http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML"
s = urllib2.urlopen(url)
print s

tree = ElementTree.parse(s)
print tree

root = tree.getroot()
print root


for child in root:
    print "Description" ,child[1].text
    print "Latitude:" ,child[3].text
    print "Longitude:" ,child[4].text
    print "Code:" ,child[5].text
    print "ID:" ,child[6].text
    print "----------------------------"
