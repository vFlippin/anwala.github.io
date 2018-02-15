#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
#import urllib2
from urllib.request import urlopen

# This script uses HEAD requests (with fallback in case of 405) 
# to follow the redirect path up to the real URL
# (c) 2012 Filippo Valsorda - FiloSottile
# Released under the GPL license

class HeadRequest#(urllib2.Request):
    def get_method(self):
        return "HEAD"

class HEADRedirectHandler(urllib2.HTTPRedirectHandler):
    """
    Subclass the HTTPRedirectHandler to make it use our 
    HeadRequest also on the redirected URL
    """
    def redirect_request(self, req, fp, code, msg, headers, newurl): 
        if code in (301, 302, 303, 307):
            newurl = newurl.replace(' ', '%20') 
            newheaders = dict((k,v) for k,v in req.headers.items()
                              if k.lower() not in ("content-length", "content-type"))
            return HeadRequest(newurl, 
                               headers=newheaders,
                               origin_req_host=req.get_origin_req_host(), 
                               unverifiable=True) 
        else: 
            raise urllib2.HTTPError(req.get_full_url(), code, msg, headers, fp) 
            
class HTTPMethodFallback(urllib2.BaseHandler):
    """
    Fallback to GET if HEAD is not allowed (405 HTTP error)
    """
    def http_error_405(self, req, fp, code, msg, headers): 
        fp.read()
        fp.close()

        newheaders = dict((k,v) for k,v in req.headers.items()
                          if k.lower() not in ("content-length", "content-type"))
        return self.parent.open(urllib2.Request(req.get_full_url(), 
                                         headers=newheaders, 
                                         origin_req_host=req.get_origin_req_host(), 
                                         unverifiable=True))

# Build our opener
opener = urllib2.OpenerDirector() 
for handler in [urllib2.HTTPHandler, urllib2.HTTPDefaultErrorHandler,
                HTTPMethodFallback, HEADRedirectHandler,
                urllib2.HTTPErrorProcessor, urllib2.HTTPSHandler]:
    opener.add_handler(handler())

response = opener.open(HeadRequest(sys.argv[1]))

print (response.geturl())
