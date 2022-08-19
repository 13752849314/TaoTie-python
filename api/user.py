# Created by 敖鸥 at 2022/8/11
from flask import Blueprint, request
from result import Result
from service.filter import jwt_filter
from service.dbutils import select_by_name, update_info

user = Blueprint('user', __name__)


@user.route('/add', methods=['POST'])
@jwt_filter
def add():
    return Result.SUCCESS('success!').push('ty', 777).build()


@user.route('/userInfo', methods=['POST'])
@jwt_filter
def user_info():
    username = request.json.get('username')
    user1 = select_by_name(username)
    return Result.SUCCESS('用户信息获取成功!').push('userInfo', user1.get_info()).build()


@user.route('/reset_info', methods=['POST'])
@jwt_filter
def reset_information():
    username = request.json.get('username')
    user1 = select_by_name(username)
    info_dict = {k: v for k, v in request.json.items() if k in ['phone', 'email', 'sex', 'birthday']}
    num = update_info(user1.reset_info(**info_dict))
    if num is Exception:
        return Result.FAIL('更新失败!').build()
    else:
        return Result.SUCCESS('更新成功!').build()


@user.route('/resetPW', methods=['POST'])
@jwt_filter
def reset_password():
    username = request.json.get('username')
    password = request.json.get('new_pw')
    user1 = select_by_name(username)
    user1.password = password
    
    pass
