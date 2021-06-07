import requests

print(requests.get('https://whoami.quoccabank.com', cert=('/home/fafnir/cert/6843.pem', '/home/fafnir/cert/6843.key')).text);
