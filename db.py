# Created by 敖鸥 at 2022/8/9
import pymysql, time
from dbutils.pooled_db import PooledDB

print('db init start! ->', time.time())
POOL = PooledDB(
    creator=pymysql,
    maxconnections=5,  # 最大连接数
    mincached=2,  # 初始化时连接池中至少创建的连接
    blocking=True,  # 要等待

    host='127.0.0.1',
    port=3306,
    user='root',
    password='hg5200820',
    database='mutex',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor  # 返回字典类型
)
print('db init finish! ->', time.time())
"""
conn = POOL.connection()
cursor = conn.cursor()

cursor.execute('select * from users')

result = cursor.fetchall()
cursor.close()
conn.close()

print(result)
print(type(result[0]))
"""
