import math
import requests
import urllib
from bs4 import BeautifulSoup
import re





def get():
    path="calculator/"
    cert= ('/home/fafnir/cert/6843.pem', '/home/fafnir/cert/6843.key');


    url='https://haas.quoccabank.com'
    payload = 'GET /'+path+' HTTP/1.1\nhost: kb.quoccabank.com'
    obj = {'request': payload}
    obj= urllib.parse.urlencode(obj)
    response = requests.post(url, params=obj, cert=cert)
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.prettify())

    #set cookie
    cookie = ""
    cookie_res = re.search('calc=.+;', response.text)
    try:
        cookie = cookie_res.group(0)[:-1]
    except:
        print('err has occurred')
    
    #arithmetics
    arith = ""
    arith_res = re.search('What is ([0-9]*\+[0-9]*)', response.text)
    arith = arith_res.group(1)

    answer = str(eval(arith))

    content_length = str(7+len(answer))
    
    post(content_length, cookie, answer)
    


    


def post(content_length, cookie, answer):
    path="calculator/"
    cert= ('/home/fafnir/cert/6843.pem', '/home/fafnir/cert/6843.key');
    url='https://haas.quoccabank.com'
    payload = 'POST /calculator/ HTTP/1.1\nHost: kb.quoccabank.com\nContent-Length: '+content_length+'\nOrigin: haas.quoccabank.com\nContent-Type: application/x-www-form-urlencoded\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\nReferer: haas.quoccabank.com\nAccept-Encoding: gzip, deflate\nAccept-Language: en-GB,en-US;q=0.9,en;q=0.8\nConnection: close\nCookie: '+cookie+'\n\nanswer='+answer

    #print(payload)

    obj = {'request': payload}
    obj= urllib.parse.urlencode(obj)
    response = requests.post(url, params=obj, cert=cert)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())


get()

