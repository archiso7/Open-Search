from Fun import crawl

#define lists
f = open("sites.txt", "r")
urls = str(f.read()).strip('][').replace("\'", '').replace("\"", '').split(', ')
f.close()
if(urls == ""):
    base_urls = ['https://en.wikipedia.org/wiki/Main_Page']
else:
    base_urls = urls

#ask for number of urls to search

numurls = input("How many more urls would you like to find? ")

#scrape for urls
crawl(base_urls, numurls)

#write to sites file
f = open("sites.txt", "w")
f.write(str(urls))
f.close()