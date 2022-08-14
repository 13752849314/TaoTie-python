# Created by 敖鸥 at 2022/8/10
import time


class User:
    def __init__(self,
                 id=0,
                 username='',
                 password='',
                 phone='',
                 email='',
                 sex='',
                 birthday=None,
                 state=0):
        self.id = id
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.sex = sex
        self.birthday = birthday
        self.state = state
        self.birthday = self.format_date(self.birthday)

    def get_info(self):
        re_dict = {k: v for k, v in self.__dict__.items() if k not in ['id', 'password', 'state']}
        return re_dict

    @classmethod
    def format_date(cls, birthday):
        if birthday is None:
            return time.strftime('%Y-%m-%d', time.gmtime())
        elif birthday is str:
            return birthday
        else:
            return birthday.strftime('%Y-%m-%d')
