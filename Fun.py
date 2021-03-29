#imports for scraping websites
from bs4 import BeautifulSoup
from requests import get

#define some variables
containlst = []
headers = {
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4446.0 Safari/537.36'
}

#search for query
def search1(url, search):
        toRead = get(url, headers=headers)
        content = str(BeautifulSoup(toRead.content, "html.parser"))[1:]
        content = remove(content)
        nonewline = str(content)
        content = nonewline.replace(' ', "")
        searchlst = search.split()
        relevance = 0
        for query in searchlst:
            relevance += content.count(query)
        containlst.append(relevance)
        print(containlst)

#remove html tags
def remove(test_str):
    ret = ''
    skip1c = 0
    for i in test_str:
        if i == '<':
            skip1c += 1
        elif i == '>' and skip1c > 0:
            skip1c -= 1
        elif skip1c == 0:
            ret += i
    return ret

#take urls from websites
def extract(soup, base_url):
    outlst = []
    for link in soup.findAll('a'):
        url = str(link.get('href'))
        if(url not in outlst):
            if(url.startswith("http")):
                print(url)
                outlst.append(url)
            elif(url.startswith("//")):
                url = "http:" + url
                print(url)
                outlst.append(url)
            elif(url.startswith("/")):
                url = base_url[:findnth(base_url, "/", 3)] + url
                print(url)
                outlst.append(url)
    return outlst

#find the nth term in a string or list
def findnth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

#scrape websites for urls
def crawl(lst):
    savelst = lst
    depth = 1
    for i in savelst:
        print(i)
        mush = get(i, headers=headers)
        content = BeautifulSoup(mush.content, "html.parser")
        while(depth < 10):
            for link in extract(content, i):
                if(link not in savelst):
                    print(link)
                    savelst.append(link)
                depth += 1
    return savelst