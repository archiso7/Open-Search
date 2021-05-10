from Fun import crawl
from os import path

#define lists
base_urls = ['https://en.wikipedia.org/wiki/Main_Page']
if(path.exists("sites.txt")):
    f = open("sites.txt", "r")
    urls = str(f.read()).strip('][').replace("\'", '').replace("\"", '').split(', ')
    print(base_urls[0])
    if(base_urls[0] == urls[0]):
        base_urls = urls
    f.close()
else:
    f = open("sites.txt", "w+")
    f.write(str(base_urls))
    urls = str(f.read()).strip('][').replace("\'", '').replace("\"", '').split(', ')
    f.close()

#ask for number of urls to search
numurls = input("How many more urls would you like to find? ")
isint = 0
while(isint == 0):
    isint = 1
    try:
        numurls = int(numurls)
    except ValueError:
        isint = 0

#scrape for urls
urls = crawl(base_urls, numurls)

#write to sites file
f = open("sites.txt", "w")
f.write(str(urls))
f.close()