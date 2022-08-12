# Created by 敖鸥 at 2022/8/10


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
