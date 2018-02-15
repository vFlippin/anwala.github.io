#add urls to list until 1000 added.  check for double before adding
#manually check 1st 10 url in list to ensure not double, get the list started
import sys

input_file = open(sys.argv[1],'r')
urlSet = [input_file.readline().strip()]
for x in range(0, 8):
    urlSet = urlSet + [input_file.readline().strip()]

urlSet.sort()
for line in input_file:
    #def find(urlSet, url):
    url = line
    start = 0
    end = len(urlSet) - 1
    while start <= end:
        middle = (start + end)// 2
        midpoint = urlSet[middle]
        if midpoint > url:
            end = middle - 1
        elif midpoint < url:
            start = middle + 1
        elif midpoint == url:
            null #do nothing
        else:
            urlSet.insert(middle,url)
        

