#import stuff from Fun.py
from Fun import search1
from Fun import crawl
from Fun import containlst
#import futures for multithreading
import concurrent.futures

#define lists
outurls = []
base_urls = ['https://en.wikipedia.org/wiki/Main_Page']

#scrape for urls
urls = crawl(base_urls)

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