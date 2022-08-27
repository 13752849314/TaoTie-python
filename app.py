from flask import Flask
from api.common import com
from api.user import user
from flask_cors import CORS

from result import Result

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(com)
app.register_blueprint(user, url_prefix='/user')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    return Result.SUCCESS('test').push('data', 123).build()


if __name__ == '__main__':
    app.run()
