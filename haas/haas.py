import requests
import urllib
from bs4 import BeautifulSoup
import re

def crawl(path):
    url='https://haas.quoccabank.com'
    payload = 'GET '+path+' HTTP/1.1\nhost: kb.quoccabank.com'
    obj = {'request': payload}
    obj= urllib.parse.urlencode(obj)
    response = requests.post(url, params=obj, cert=cert)

    path=path[:len(path)-1]
    #print(f'path=${path}')

    print(response.text)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        '''
        content
        '''
        #print(response.content.decode('utf-8'))
        try:
            match = re.search(r'COMP6443', response.content.decode('utf-8'))
            print(match.string)
        except:
            pass
        links = [ path + re.sub(r'^\.', '', x['href']) for x in soup.find_all('a')]
        #print(links)

        return links

    else:
        return []

path=""
cert= ('/home/fafnir/cert/6843.pem', '/home/fafnir/cert/6843.key');
url='https://haas.quoccabank.com'
payload = 'GET /'+path+' HTTP/1.1\nhost: kb.quoccabank.com'
obj = {'request': payload}
obj= urllib.parse.urlencode(obj)

response = requests.post(url, params=obj, cert=cert)

soup = BeautifulSoup(response.content, 'html.parser')

deep= soup.find_all('a')[1]
path = deep['href']

links = crawl(path)

print(len(links))
while(links):
    path = links.pop(0)
    links.extend(crawl(path))

print(links)

'''
response = requests.post(url, params=obj, cert=cert)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())
'''

