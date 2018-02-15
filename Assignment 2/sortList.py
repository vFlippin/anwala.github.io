import sys

input_file = open(sys.argv[1],'r')
urlList = []
for line in input_file:
    urlList = urlList + [line.strip()]
	
urlList.sort()


size = len(urlList)
print (len(urlList))
for x in range(size -2 , -1, -1):
    if urlList[x] == urlList[x+1]:
        urlList.pop(x-size+1)
        size = len(urlList)

for x in range(0, len(urlList)-1):
    print(urlList[x])