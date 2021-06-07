import requests

s = requests.Session()
s.cert = ('/home/fafnir/cert/6843.pem', '/home/fafnir/cert/6843.key');
print(s.get('https://whoami.quoccabank.com').text);
