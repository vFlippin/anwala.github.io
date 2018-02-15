#need to curl each url in a text file, output good uri [returns 200] to a new text file

import traceback
import httplib2
from urllib.request import urlopen
import sys

input_file = open(sys.argv[1],'r') #
# h = httplib2.Http()

def genericErrorInfo():
	import os, sys
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	errorMessage = fname + ', ' + str(exc_tb.tb_lineno)  + ', ' + str(sys.exc_info())
	print('\tERROR:', errorMessage)

for line in input_file:
    try:
        code = 0
        url = line.strip()
        #line = line[:-1]
        #print(len(url))
        #print ('trying ' + url)
        response = urlopen(url)
        code = response.getcode()
        #print ('status is '+ response.getcode())
        if code == 200:
            print (url)
        #else:
            #print('not 200, was ' + response.getcode())
    except:
        #genericErrorInfo()
        continue