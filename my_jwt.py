# Created by 敖鸥 at 2022/8/10
import jwt
import threading
import time
import uuid
import datetime

import schedule

print('jwt init start! ->', time.time())

MINUTE = 10
DAY = 7
JWT_MAX_LEN = 10
_SALT = 'happyGhostAndItFatherAndStudent12or456#!?LOVEcQuPt'


class MyJWT:
    @classmethod
    def generate_jwt(cls, payload, expiry, secret=_SALT):
        """
        生成JWT
        :param payload: 载荷
        :param expiry: 有效期
        :param secret: 秘钥
        :return:
        """
        _payload = {'exp': expiry}
        _payload.update(payload)

        JWT = jwt.encode(_payload, secret, algorithm='HS256')
        return JWT

    @classmethod
    def verify_jwt(cls, Jwt, secret=_SALT):
        try:
            payload = jwt.decode(Jwt, secret, algorithms=['HS256'])
        except jwt.PyJWKError:
            payload = None
        return payload


class Token:
    tokens = []
    mes = dict()
    my_jwt = []

    def create_token(self):
        token = str(uuid.uuid4())
        self.tokens.append({
            "token": token,
            "time": time.time()
        })
        return token


def check(to: Token, minute):
    tmp = []
    tokens_tmp = []
    for i in to.tokens:
        if time.time() - i.get('time') < 60 * minute:
            tmp.append(i)
        else:
            # print('token->', i.get('token'), '-> out of date!')
            token = i.get('token')
            tokens_tmp.append(token)
    D = to.mes.copy()
    for k, v in D.items():
        if v[1] == 1 and v[0] in tokens_tmp:
            to.mes.pop(k)
    to.tokens = tmp


def check_jwt(to: Token):
    if len(to.my_jwt) > JWT_MAX_LEN:
        to.my_jwt = to.my_jwt[(len(to.my_jwt) - JWT_MAX_LEN):]
    tmp = []
    for i in to.my_jwt:
        payload = MyJWT.verify_jwt(i)
        if payload is None:
            tmp.append(i)
        else:
            exp = payload.get('exp')
            if int(time.time()) >= exp:
                tmp.append(i)
    for i in tmp:
        to.my_jwt.remove(i)


a = Token()


def tag():
    schedule.every(MINUTE).minutes.do(check, to=a, minute=MINUTE)
    schedule.every(DAY).days.do(check_jwt, to=a)

    while True:
        schedule.run_pending()


T = threading.Thread(target=tag)
T.start()
print('jwt init finish! ->', time.time())

if __name__ == '__main__':
    J = MyJWT.generate_jwt({'username': 'hg'}, datetime.datetime.now())
    print(J)
    b = MyJWT.verify_jwt(J)
    print(b)
    print(type(b['exp']))
