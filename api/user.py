# Created by 敖鸥 at 2022/8/11
from flask import Blueprint
from result import Result
from service.filter import jwt_filter

user = Blueprint('user', __name__)


@user.route('/add', methods=['POST'])
@jwt_filter
def add():
    return Result.SUCCESS('success!').push('ty', 777).build()
