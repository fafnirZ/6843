import math
import requests
import urllib
from bs4 import BeautifulSoup


def get():
    path="calculator/"
    cert= ('/home/fafnir/cert/6843.pem', '/home/fafnir/cert/6843.key');
    url='https://haas.quoccabank.com'
    payload = 'GET /'+path+' HTTP/1.1\nhost: kb.quoccabank.com'
    obj = {'request': payload}
    obj= urllib.parse.urlencode(obj)
    response = requests.post(url, params=obj, cert=cert)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())

def post():
    path="calculator/"
    cert= ('/home/fafnir/cert/6843.pem', '/home/fafnir/cert/6843.key');
    url='https://haas.quoccabank.com'
    payload = 'POST /'+path+' HTTP/1.1\nhost: kb.quoccabank.com\n'
    obj = {'request': payload}
    obj= urllib.parse.urlencode(obj)
    response = requests.post(url, params=obj, cert=cert)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
