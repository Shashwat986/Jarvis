import sys
import re
import urllib2
import urlparse
from bs4 import BeautifulSoup

url='http://www.google.com/search?q="'
string=""
for v in sys.argv[1:]:
	url+=str(v)+"+"
	string+=str(v)+" "
url=url[:-1]+'"'
string=string[:-1]

link="http://www.food.com/recipe-collection/banana-pie"

try:
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

	headers={'User-Agent':user_agent,} 
	request=urllib2.Request(link,None,headers)
	response = urllib2.urlopen(request)
except:
	print 'lol'
	sys.exit(0)

msg=response.read()


print string
rx=re.compile(r"(^|[.>!?])(.*?)("+string+r")(.*?)([.<!?]|$)",flags=re.IGNORECASE)
m=rx.search(msg)
print m
print m.group(0)
