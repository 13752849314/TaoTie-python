# Created by 敖鸥 at 2022/8/9
import functools

from flask import request, jsonify

from my_jwt import MyJWT, a
from result import Result
from service.dbutils import (select_by_name)


def code_filter(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = request.json
        code = key.get('code')
        token = a.mes.get(code)
        if token is None:
            return jsonify(Result.FAIL('验证码错误!').__dict__)
        else:
            if token[0] != key.get('token'):
                return jsonify(Result.FAIL('验证码已过期!').__dict__)
        return func(*args, **kwargs)

    return inner


def username_password_filter(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = request.json
        # print('username_password_filter', key)
        username = key.get('username')
        password = key.get('password')
        user = select_by_name(username)
        # print(user)
        if user is None:
            return jsonify(Result.FAIL('用户不存在!').__dict__)
        else:
            if user.password != password:
                return jsonify(Result.FAIL('密码错误!').__dict__)
        return func(*args, **kwargs)

    return inner


def username_filter(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('username_filter')
        key = request.json
        username = key.get('username')
        user = select_by_name(username)
        if user is not None:
            return jsonify(Result.FAIL('用户名已经存在!').__dict__)
        # else:
        #     e = insert(key)
        #     # print('e=', e)
        #     if e is Exception:
        #         return jsonify(Result.FAIL('系统出错!').__dict__)
        return func(*args, **kwargs)

    return inner


def jwt_filter(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        authorization = request.headers.get('Authorization', '')
        if authorization == '':
            return Result.FAIL('用户未登录!').build()
        else:
            if authorization in a.my_jwt:
                bo = MyJWT.verify_jwt(authorization)
                if bo is None:
                    return Result.FAIL('JWT错误!').build()
                else:
                    name = bo.get('username', '')
                    # print('name=', name, 'json=', request.json.get('username'))
                    if name != request.json.get('username'):
                        return Result.FAIL('越权!').build()
            else:
                return Result.FAIL('登录已过期!').build()
        return func(*args, **kwargs)

    return inner
