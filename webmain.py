#imports
from Fun import search1
from Fun import containlst

#define list
outurls = []

#get urls
f = open("sites.txt", "r")
urls = str(f.read()).strip('][').replace("\'", '').replace("\"", '').split(', ')
print(urls)
f.close()
if(urls == ""):
	print("There are no urls. Run crawler.py to find some.")
else:
	#get query from user
	search = input("Search:\n")

	#search for query
	for url in urls:
		search1(url, search)

	#order the results
	for i in urls:
		larnumpos = 0
		larnum = 0
		count = 0
		while(count < len(containlst)):
			if(containlst[count] > larnum):
				larnum = containlst[count]
				larnumpos = count
			count += 1
		outurls.append(urls[larnumpos])
		urls.pop(larnumpos)
		containlst.pop(larnumpos)

	#add the last url and print
	outurls.append(urls[0])
	print(outurls)