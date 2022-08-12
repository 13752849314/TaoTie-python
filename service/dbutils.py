# Created by 敖鸥 at 2022/8/10
from db import POOL
from enity.tables import User


def get_connect():
    return POOL.connection()


def close(cursor, conn):
    cursor.close()
    conn.close()


# users

def select_by_name(name):
    conn = get_connect()
    cursor = conn.cursor()
    sql = "select * from users where username=%s"
    num = cursor.execute(sql, [name])
    if num == 0:
        return None
    result = cursor.fetchone()

    close(cursor, conn)
    return User(**result)


def insert(kwargs):
    conn = get_connect()
    cursor = conn.cursor()
    user = User(**kwargs)
    # print(user.__dict__)
    sql = "insert into users values (%s, %s, %s, %s, %s, %s, %s, %s)"
    arg = [v for _, v in user.__dict__.items()]
    # for i in arg:
    #     print(i)
    try:
        num = cursor.execute(sql, arg)
        conn.commit()
        return num
    except Exception as e:
        conn.rollback()
        return e
    finally:
        close(cursor, conn)
