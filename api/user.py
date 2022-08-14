# Created by 敖鸥 at 2022/8/11
from flask import Blueprint, request
from result import Result
from service.filter import jwt_filter
from service.dbutils import select_by_name

user = Blueprint('user', __name__)


@user.route('/add', methods=['POST'])
@jwt_filter
def add():
    return Result.SUCCESS('success!').push('ty', 777).build()


@user.route('/userInfo', methods=['POST'])
@jwt_filter
def userInfo():
    username = request.json.get('username')
    user1 = select_by_name(username)
    return Result.SUCCESS('用户信息获取成功!').push('userInfo', user1.get_info()).build()
