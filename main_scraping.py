#import requests
import ScrapFunction
from urllib.request import urlopen
from bs4 import BeautifulSoup
#title=getTitle("https://pantip.com/forum/sinthorn")
#title=getTitle("https://peagateway.pea.co.th/vpn/tmindex.html")
#url="https://www.dafabet.com/th/sports-df/sports"
url="https://www.pea.co.th/"

title=ScrapFunction.getTitle(url)
if title == None:
    print("title not found")
else:
    print("***title below here***")
    print(title)
    #print(title[0].get_text())
    #for name in title:
        #print(name.get_text())

#print(bs_obj.html)
#print(bs_obj.head)
#print(bs_obj.title)

#print(bs_obj.body)
#print(bs_obj.h1)
#print(bs_obj.div)

body=ScrapFunction.getBody(url)
if body == None:
    print("body not found")
else:
    print("***body below here***")
    print(body)

textList=ScrapFunction.getText(url)
if textList == None:
    print("text not found")
else:
    print("***text below here***")
    for text in textList:
        print(text.get_text())

head=ScrapFunction.getHead(url)
if head == None:
    print("head not found")
else:
    print("***head below here***")
    print(head)

linkList=ScrapFunction.getLink(url)
if linkList == None:
    print("url not found")
else:
    print("***link below here***")
    for link in linkList:
        if "href" in link.attrs:
            print(link.attrs["href"])
imgList=ScrapFunction.getImg(url)
if imgList == None:
    print("url not found")
else:
    print("***link image below here***")
    for img in imgList:
        #if "data-src" in img.attrs:
        print(img.attrs["data-src"])
        print(img.attrs["src"])

        #print(img)