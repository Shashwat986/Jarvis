import sys
import re
import urllib2
import urlparse
from bs4 import BeautifulSoup
tocrawl = set([sys.argv[1]])
crawled = set([])
keywordregex = re.compile('<meta\sname=["\']keywords["\']\scontent=["\'](.*?)["\']\s/>')
linkregex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')

try:
	while 1:
		try:
			crawling = tocrawl.pop()
			print crawling
		except KeyError, e:
			raise StopIteration
		url = urlparse.urlparse(crawling)
		try:
			response = urllib2.urlopen(crawling)
		except:
			continue
		msg = response.read()
		
		soup = BeautifulSoup(msg)
		title = soup.title.string
		print title
		
		keywordlist = keywordregex.findall(msg)
		if len(keywordlist) > 0:
			keywordlist = keywordlist[0]
			keywordlist = keywordlist.split(", ")
			print keywordlist
		
		links = [tag.get('href') for tag in soup.find_all('a') if tag.get('href')!=None]
		
		crawled.add(crawling)
		
		for link in links:
			if link==None:
				continue
			if link.startswith('/'):
				link = 'http://' + url[1] + link
			elif link.startswith('#'):
				link = 'http://' + url[1] + url[2] + link
			elif not link.startswith('http'):
				link = 'http://' + url[1] + '/' + link
			if link not in crawled:
				tocrawl.add(link)
except KeyboardInterrupt:
	print len(crawled),'/',(len(tocrawl)+len(crawled))