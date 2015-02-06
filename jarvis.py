import re
import sys
import os
import glob

words=sys.argv[1:]

dirs=[d for d in os.listdir('.') if os.path.isdir(d)]


if words[0] in dirs:
	str=" ".join(words)
	f=open("./"+words[0]+"/syntax.txt",'r')
	lines=f.readlines()
	for line in lines:
		try:
			[rege,form,code]=line.split('|||')
		except ValueError:
			print "Syntax incomplete"
			rege=line.split('|||')
			rege=rege[0];
			form='';
			code='';
		
		rege=rege.strip()
		form=form.strip()
		code=code.strip()
		res=re.match(rege,str)
		if res:
			print res.group()
			print rege
			if form:
				print form
				
			break
			