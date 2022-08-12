# Created by 敖鸥 at 2022/8/9
from flask import jsonify


class Result:
    def __init__(self, **kwargs):
        self.code = kwargs.get('code')
        self.message = kwargs.get('message')
        self.data = dict()

    @classmethod
    def SUCCESS(cls, message):
        return Result(code=200, message=message)

    @classmethod
    def FAIL(cls, message):
        return Result(code=400, message=message)

    def push(self, key, value):
        self.data[key] = value
        return self

    def build(self):
        return jsonify(self.__dict__)


if __name__ == '__main__':
    re = Result.SUCCESS("123")
    re = re.push(1, 123).push('123', '4567')
    print(re.__dict__)

    a = Result(code='123')
    print(a.__dict__)
