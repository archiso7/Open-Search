from Fun import crawl

#define lists
f = open("sites.txt", "r")
urls = str(f.read()).strip('][').replace("\'", '').replace("\"", '').split(', ')
f.close()
if(urls == ""):
    base_urls = ['https://en.wikipedia.org/wiki/Main_Page']
else:
    base_urls = urls

#scrape for urls
crawl(base_urls)

#write to sites file
f = open("sites.txt", "w")
f.write(str(urls))
f.close()