from itsdangerous import Signer
import jwt
'''
dbg_option="-shell-escape"
skey='imagineUsingW0rd'

s = Signer(skey)
signed = s.sign(dbg_option).decode('utf-8')
print(signed)

'''
value='539f98bf-9a52-4bc0-bf34-1ffaba10997c'
key='-----BEGIN PUBLIC KEY-----\nMCowBQYDK2VwAyEAvN+9X61kkoKeD5Nzx4je0fZAkSfSEMwCXz/pdIBIMdU=\n-----END PUBLIC KEY-----'
print(jwt.decode(value,key, algorithms=['EdDsa']))
