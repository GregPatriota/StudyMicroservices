from flask import Flask, Response
from json import dumps

app = Flask(__name__)


@app.route('/')
def hello_world():
    return Response(response=dumps({'msg': 'Hello World'}),
                    content_type='Application/json',
                    status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
