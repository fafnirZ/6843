import requests
import urllib
from bs4 import BeautifulSoup
import re

def crawl_dfs(path):
    url='https://haas.quoccabank.com'
    payload = 'GET '+path+' HTTP/1.1\nhost: kb.quoccabank.com'
    obj = {'request': payload}
    obj= urllib.parse.urlencode(obj)
    response = requests.post(url, params=obj, cert=cert)
    soup = BeautifulSoup(response.content, 'html.parser')
    path = path[:-1]

    #print(response.text)

    for link in soup.find_all('a'):
        link = link['href'][1:]
        child = "/deep"+link
        if(child not in ht):
            ht[child] = 1
            crawl_dfs(path)
        else:
            continue

    return 
'''
initialisation
'''
path=""
cert= ('/home/fafnir/cert/6843.pem', '/home/fafnir/cert/6843.key');
url='https://haas.quoccabank.com'
payload = 'GET /'+path+' HTTP/1.1\nhost: kb.quoccabank.com'
obj = {'request': payload}
obj= urllib.parse.urlencode(obj)
response = requests.post(url, params=obj, cert=cert)
soup = BeautifulSoup(response.content, 'html.parser')
ht = {}

#initial question for deep
deep= soup.find_all('a')[1]
path = deep['href'][:len(deep['href'])]

crawl_dfs(path)

