from flask.sessions import TaggedJSONSerializer
from itsdangerous import TimestampSigner, URLSafeTimedSerializer
import hashlib
import base64

secret='$hallICompareTHEE2aSummersday'
data={"role":"Admin","username":"jack"}


#encoded = base64.b64encode(data.encode()).decode()

#s = TimestampSigner(secret)
#result = s.sign(data)
#print(result)
#data = result.decode().split('.')[1:]
#data.insert(0, encoded)
#print('.'.join(data))

serializer = URLSafeTimedSerializer(
    secret_key=secret,
    signer=TimestampSigner,
    signer_kwargs={
        'key_derivation':'hmac',
        'digest_method': hashlib.sha1
    }
).load(data)

print(serializer)



