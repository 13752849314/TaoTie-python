from flask import Flask
from api.common import com
from api.user import user
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(com)
app.register_blueprint(user, url_prefix='/user')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
