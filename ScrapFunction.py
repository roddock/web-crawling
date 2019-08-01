from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
def getBody(url):#get body of page
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs_obj = BeautifulSoup(html,"html.parser")
        body = bs_obj.body
    except AttributeError as e:
        return None
    return body
def getTitle(url):#get title name page
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs_obj = BeautifulSoup(html,"html.parser")
        #title = bs_obj
        title = bs_obj.title

        #title = bs_obj.head
        #title = bs_obj.findAll("link", {"href": "/fav-icon.icon"}) #tag in head
        #title = bs_obj.findAll("link",{"rel":"icon"})#tag in head
        #title = bs_obj.findAll("link",{"rel":"icon"})#tag in head

        #title = bs_obj.body
        #title = bs_obj.findAll("span", {"class": "title"})#tag in body
        #title = bs_obj.findAll("div", {"class": "post-item-title"}) # tag in body

    except AttributeError as e:
        return None
    return title
def getText(url):#get body of page
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs_obj = BeautifulSoup(html,"html.parser")
        textList = bs_obj.findAll("span",{"class":"title"})
        #textList = bs_obj.findAll("header", {"class": "header"})
        #textList = bs_obj.findAll("a", {"class": "main-menu-link"})#

    except AttributeError as e:
        return None
    return textList
def getHead(url):#get head of page
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs_obj = BeautifulSoup(html,"html.parser")
        headList = bs_obj.head
    except AttributeError as e:
        return None
    return headList

def getLink(url):  # get link of page
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs_obj = BeautifulSoup(html, "html.parser")
        linkList = bs_obj.findAll("a",{"class": "main-menu-link"})
        #linkList = bs_obj.findAll("a")
    except AttributeError as e:
        return None
    return linkList
def getImg(url):  # get link of image
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs_obj = BeautifulSoup(html, "html.parser")
        imgList = bs_obj.findAll("img",{"data-src":re.compile("\/*\/*\/*\/*\.png")})

    except AttributeError as e:
        return None
    return imgList




