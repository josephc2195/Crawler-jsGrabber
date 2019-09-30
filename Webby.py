import sys
import requests
import re
from bs4 import BeautifulSoup as soup

url = soup(requests.get(sys.argv[1]).content).find_all("script")

on_page = []
off_page = []

for i in url:
    try:
        off_page.append(i['src'])
    except KeyError:
        on_page.append(i)

with open('jsDownload.js', 'w') as js:
    js.write('// All the JavaScript in this page. \n\n')
    for i in on_page:
        js.write(i.text  + '\n')
    js.write('// All the JavaScript off the page. \n\n')
    for i in off_page:
        if re.match(r'http', i):
            js.write(requests.get(i).content + "\n")
        elif re.match(r'/', i):
            js.write(requests.get(f"{sys.argv[1]}{i}").content + '\n')
        else:
            js.write(requests.get(f"{sys.argv[1]}/{i}").content + '\n')
