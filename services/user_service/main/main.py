from flask import Flask, Response
from json import dumps
from flask_nameko import FlaskPooledClusterRpcProxy

app = Flask(__name__)
rpc = FlaskPooledClusterRpcProxy()
app.config.update(dict(
        NAMEKO_AMQP_URI='amqp://guest:guest@localhost:5672'
    ))

rpc.init_app(app)


@app.route('/')
def hello_world():
    return Response(response=dumps({'msg': 'Hello World'}),
                    content_type='Application/json',
                    status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)