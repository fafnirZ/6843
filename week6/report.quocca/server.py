from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

APP = Flask(__name__)
CORS(APP, supports_credentials=True)


@APP.route('/')
@cross_origin(origins="report.quoccabank.com")
def ret():
    response = jsonify(success=True)
    response.headers.add("Access-Control-Allow-origin", "https://report.quoccabank.com")
    response.headers.add("Access-Control-Allow-Credentials", 'true')
    return response

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=4444)
