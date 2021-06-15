import requests
import urllib
from bs4 import BeautifulSoup
import re
import sys
import time

'''
argv_1 = domain
argv_2 = wordlist
'''


def create_request(domain, path, sleep, count_200):
    host = 'https://'+domain
    url = host+'/'+path
    cert = ('/home/fafnir/cert/6843.pem', '/home/fafnir/cert/6843.key')
    burp0_cookies = {"wordpress_test_cookie": "WP%20Cookie%20check", "wordpress_logged_in_239843576ca445946581af59b0353047": "admin%7C1623898956%7CBecnyRk17EPEXiwQ7BNCORAyPQa8FLUJA2Dfmzbzco3%7Cea1adbdd6b891278d22f1703edb618f3f4cf675858b5eb19fb26fc7caa6766f4", "wp-settings-1": "mfold%3Do", "wp-settings-time-1": "1623726156"}
    burp0_headers = {"Sec-Ch-Ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"", "Sec-Ch-Ua-Mobile": "?0", "Upgrade-Insecure-Requests": "1", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Connection": "close"}
    response = requests.get(url, headers=burp0_headers, cookies=burp0_cookies, cert=cert)
    print(f'status code = {response.status_code} path={url}')
    #print(response.text)
    if(response.status_code == 200):
        if(count_200 > 10):
            #print('resetting throttle')
            return (0, 0)
        return (sleep, count_200+1)


    if(response.status_code == 429):
        time.sleep(sleep+0.5)
        print(f'throttling for {sleep+0.5}s')
        return (sleep+0.5, 0)
    
    #default rate limit
    time.sleep(0.5)

    return(sleep,count_200)

     
    	

domain = sys.argv[1]
wordlist = sys.argv[2]
words = []
sleep = 0
count_200 = 0
with open(wordlist) as file:
    data = file.read()
    words = list(data.split('\n'))
    
for word in words:
    sleep, count_200 = create_request(domain, word, sleep, count_200)







