from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os

APP = Flask(__name__)
CORS(APP, supports_credentials=True)


@APP.route('/require')
@cross_origin(origins=["www.test-cors.org","report.quoccabank.com", "localhost:3000"])
def ret():
    print(request.headers)

    response = jsonify(success=True)
    #response.headers.add("Access-Control-Allow-origin","https://report.quoccabank.com","https://www.test-cors.org/")
    #response.headers.add("Access-Control-Allow-origin", "https://www.test-cors.org")
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
    response.headers.add("Access-Control-Allow-Methods", "GET")
    response.headers.add("Access-Control-Allow-Credentials", 'true')
    response.headers.add("Set-Cookie", "_okdetect=abc; SameSite=None; Secure")
    return response

@APP.route('/')
def reaa():
    try:
        src = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'index.html')
        return Response(open(src).read(), mimetype="text/html")
        
    except IOError as exec:
        return str(exec)


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=4444)
