from urllib.request import urlopen
html = urlopen("http://172.17.1.5/")
print(html.read())
