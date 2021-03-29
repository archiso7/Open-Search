import urllib.request as urlr
from bs4 import BeautifulSoup
from lst import containlst
def search1(url, search):
        toRead = urlr.urlopen(url)
        content = str(toRead.read())[1:]
        content = remove(content)
        nonewline = str(content)
        content = nonewline.replace(' ', "")
        searchlst = search.split()
        relevance = 0
        for query in searchlst:
            relevance += content.count(query)
        containlst.append(relevance)
        print(containlst)

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

def findnth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def crawl(lst):
    savelst = lst
    depth = 1
    for i in savelst:
        print(i)
        toRead = urlr.urlopen(i)
        content = BeautifulSoup(toRead, "html.parser")
        while(depth < 10):
            for link in extract(content, i):
                if(link not in savelst):
                    print(link)
                    savelst.append(link)
                depth += 1
    return savelst