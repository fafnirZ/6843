from itsdangerous import TimestampSigner
import base64

secret_key='$hallICompareTHEE2aSummersday'
data='{"role": "Admin","username": "jack"}'

encoded = base64.b64encode(data.encode())
s = TimestampSigner('secret_key')
result = s.sign(encoded)
print(result.decode())

