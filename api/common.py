# Created by 敖鸥 at 2022/8/9
import time
from flask import Blueprint, jsonify, request
from service.image import create_image
from result import Result
from my_jwt import a, MyJWT
from service.filter import (code_filter, username_password_filter,
                            username_filter)

com = Blueprint('com', __name__)


@com.route('/image', methods=['GET'])
def get_image():
    _, strs, base = create_image()
    token = a.create_token()
    a.mes[strs] = [token, 0]
    print(strs)
    # print(type(request.headers), request.headers, request.headers.get('Authorization'), sep='\n')
    # print(type(request.headers.get('Authorization')))
    return jsonify(Result.SUCCESS('验证码获取成功').push('token', token).push('image', base).__dict__)


@com.route('/login', methods=['POST'])
@code_filter
@username_password_filter
def login():
    key = request.json
    a.mes[key.get('code')][1] = 1
    jwt = MyJWT.generate_jwt(payload={'username': key.get('username')},
                             expiry=int(time.time()) + 7 * 24 * 60 * 60)
    a.my_jwt.append(jwt)
    return jsonify(Result.SUCCESS('登录成功!').push('jwt', jwt).__dict__)


@com.route('/register', methods=['POST'])
@username_filter
def register():
    return jsonify(Result.SUCCESS('注册成功!').__dict__)
