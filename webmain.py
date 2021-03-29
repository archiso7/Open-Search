from Fun import search1
from Fun import crawl
from Fun import containlst
import urllib.request as urlr
search = input("Search:\n")
base_urls = ['https://en.wikipedia.org/wiki/Main_Page']
urls = crawl(base_urls)
for url in urls:
	search1(url, search)
outurls = []
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
outurls.append(urls[0])
print(outurls)