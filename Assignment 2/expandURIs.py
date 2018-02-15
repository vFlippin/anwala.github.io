import redirectFollower.py
import urllib2
import sys

input_file = open(sys.argv[1],'r')

for handler in [urllib2.HTTPHandler, urllib2.HTTPDefaultErrorHandler,
                HTTPMethodFallback, HEADRedirectHandler,
                urllib2.HTTPErrorProcessor, urllib2.HTTPSHandler]:
    opener.add_handler(handler())

#for line in input_file:
    #try:
#url = line.strip()
response = opener.open(HeadRequest('https://t.co/Gl7hgnkAKw'))
print (response.geturl())
	#except:
	#	continue