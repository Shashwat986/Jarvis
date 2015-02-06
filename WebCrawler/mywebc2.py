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

#print url;

urlp=urlparse.urlparse(url)
#print urlp
try:
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	
	headers={'User-Agent':user_agent,} 
	request=urllib2.Request(url,None,headers)
	response = urllib2.urlopen(request)
except:
	print "Not able to open Google"
	sys.exit(1)

msg=response.read()
soup=BeautifulSoup(msg)

links = [tag.a['href'][9:].split('&')[0] for tag in soup.find_all('li') if tag.get('class')==[u'g']]

#print links

'''
for i,link in enumerate(links):
	if link==None:
		continue
	if link.startswith('/'):
		links[i] = 'http://' + urlp[1] + link
	elif link.startswith('#'):
		links[i] = 'http://' + urlp[1] + urlp[2] + link
	elif not link.startswith('http'):
		links[i] = 'http://' + link
'''

for link in links:
	#print link
	#print '.'*80
	try:
		user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
		
		headers={'User-Agent':user_agent,} 
		request=urllib2.Request(link,None,headers)
		response = urllib2.urlopen(request)
	except:
		#print 'x'*80
		continue
	
	msg=response.read()
	
	try:
		rx=re.compile(r"(^|[.>!?])([^.>!?]*)("+string+r")([^.>!?]*)([.<!?]|$)",flags=re.IGNORECASE)
		m=rx.search(msg)
		#print m
		if m:
			print m.group(0).lstrip(' \t>.?!').strip('\t <>'),			# Currently returns just the first relevant line. Need it to return all.
		#print '-'*80
	except:
		#print 'q'*80
		continue

