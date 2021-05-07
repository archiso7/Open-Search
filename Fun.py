#imports for scraping websites
from bs4 import BeautifulSoup
from requests import get
import requests

#define some variables
containlst = []
headers = {
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4446.0 Safari/537.36'
}

#search for query
def search1(url, search):
    try:
        toRead = get(url, headers=headers,timeout=30)
    except requests.ConnectionError as e:
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))            
    except requests.Timeout as e:
        print("OOPS!! Timeout Error")
        print(str(e))
    except requests.RequestException as e:
        print("OOPS!! General Error")
        print(str(e))
    except KeyboardInterrupt:
        print("Someone closed the program")
    toRead = get(url, headers=headers)
    content = str(BeautifulSoup(toRead.content, "html.parser"))[1:]
    content = remove(content)
    nonewline = str(content)
    content = nonewline.replace(' ', "")
    searchlst = search.split()
    contentlst = content.split()
    relevance = 0
    relevance += contentlst.count(search) * 5
    for query in searchlst:
        relevance += contentlst.count(query)
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
        if(url not in outlst) and (not url.endswith(".webm")) and (not url.endswith(".ogv")) and (not url.endswith(".pdf")) and (not url.endswith(".png")):
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
            elif(url.endswith(".html") or url.endswith(".php") or url.endswith(".js") or url.endswith(".cs")):
                if(base_url.count("/") > 2):
                    url = base_url[:findnth(base_url, "/", 3)] + "/" + url
                else:
                    if(base_url.endswith("/")):
                        url = base_url + url
                    else:
                        url = base_url + "/" + url
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
def crawl(lst, numurls):
    savelst = lst
    for i in savelst:
        print(i)
        try:
            mush = get(i, headers=headers,timeout=30)
        except requests.ConnectionError as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e))            
            continue
        except requests.Timeout as e:
            print("OOPS!! Timeout Error")
            print(str(e))
            continue
        except requests.RequestException as e:
            print("OOPS!! General Error")
            print(str(e))
            continue
        except KeyboardInterrupt:
            print("Someone closed the program")
        content = BeautifulSoup(mush.content, "html.parser")
        for link in extract(content, i):
            if(numurls > 0):
                if(link not in savelst):
                    print("[" + str(numurls) + "]" + link)
                    savelst.append(link)
                    print("[lst]" + str(savelst))
                    f = open("sites.txt", "w")
                    f.write(str(savelst))
                    f.close()
                numurls -= 1
    return savelst