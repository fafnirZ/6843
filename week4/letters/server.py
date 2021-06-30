from flask import Flask

app = Flask(__name__)


@app.route('/healthz')
def fn():
    return "ok"



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8089)
