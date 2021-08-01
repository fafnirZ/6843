from flask import Flask, jsonify, render_template, make_response, request
import json
import requests


app = Flask(__name__)

@app.route('/', methods=['GET'])
def a():
    cert = ('/Users/jackyxie/documents/term2/6843/cert/6843.pem', '/Users/jackyxie/documents/term2/6843/cert/6843.key')
    req = requests.get('https://ctfproxy2.quoccabank.com/api/flagprinter-v2', cert=cert)
    try:
        print(req.text)
        print(req.headers)
        resp = jsonify(req.text)
        resp.headers.add('content-type', 'text/html')
        resp.headers.add('ctfproxy2-enabled', 1)
        return resp

    except:
        return json.dumps({})

@app.route('/internal', methods=['GET'])
def b():
    cert = ('/Users/jackyxie/documents/term2/6843/cert/6843.pem', '/Users/jackyxie/documents/term2/6843/cert/6843.key')
    req = requests.get('https://flagprinter-v2.quoccabank.com/', cert=cert)
    try:
        print(req.text)
        print(req.headers)
        resp = jsonify(req.text)
        resp.headers.add('content-type', 'text/html')
        resp.headers.add('ctfproxy2-enabled', 1)
        return resp

    except:
        return json.dumps({})

@app.route('/iframe', methods=['GET'])
def c():
    body='<!doctype html><html><body><iframe src=api/flagprinter-v2/></body></html>'
    resp=jsonify(body)
    resp.headers.add('content-type', 'text/html; charset=UTF-8')
    resp.headers.add('ctfproxy2-enabled', 1)
    return resp
@app.route('/enable/flagprinter', methods=['GET'])
def d():
    body='<!doctype html><html><body><iframe src=enable/flagprinter/></body></html>'
    resp=jsonify(body)
    resp.headers.add('content-type', 'text/html; charset=UTF-8')
    resp.headers.add('ctfproxy2-enabled', 1)
    return resp
@app.route('/iframev2', methods=['GET'])
def e():
    body='<!doctype html><html><body><script>fetch("/api/flagprinter-v2", {headers: {"ctfproxy2-enabled":"1"}})</script><b>hi</b></body></html>'
    resp=jsonify(body)
    resp.headers.add('content-type', 'text/html; charset=UTF-8')
    resp.headers.add('ctfproxy2-enabled', 1)
    return resp
@app.route('/iframev3', methods=['GET'])
def f():
    resp = make_response(render_template('template.html'))
    print(resp)
    print(type(resp))
    resp.headers.add('content-type', 'text/html; charset=UTF-8')
    resp.headers.add('ctfproxy2-enabled', '1')   
    return resp

@app.route('/ssrf', methods=['GET'])
def g():
    file = open(request.args.get('url'), 'r')
    resp = make_response(file.read())
    resp.headers.add('content-type', 'text/html; charset=UTF-8')
    resp.headers.add('ctfproxy2-enabled', '1')   
    return resp
'''
@app.after_request
def headers(resp):
    resp.headers.add('content-type', 'text/html; charset=UTF-8')
    resp.headers.add('ctfproxy2-enabled', '1')
'''


if __name__ == '__main__':
    app.run(port=4444)
