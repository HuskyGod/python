import sqlite3
import mysql.connector

# conn = sqlite3.connect('first.db')

conn = mysql.connector.connect(user='root', password = '123456', host='localhost', port='3306', database='python', use_unicode=True)

c = conn.cursor()

# c.execute('''create table user_tv(
#     _id integer primary key autoincrement,
#     name text,
#     pass text,
#     gender text
# )''')
#
# c.execute('''create table order_tb(
#     _id integer primary key autoincrement ,
#     item_name text,
#     item_price real,
#     item_number real,
#     user_id inteter,
#     foreign key(user_id) references  user_tv(_id)
# )''')

# c.execute('insert into user_tv values (null, ?, ?, ?)', ('张嘉鑫', '123456', 'make'))
# c.execute('insert into order_tb values (null, ?, ?, ?, ?)', ('张嘉鑫2', '123456', 'make', 1))

# c.executemany('insert into user_tv values(null, ?, ?, ?)',
#               (('sun', '123456', 'male'),
#                ('bai', '123456', 'famale'),
#                ('zhu', '123456', 'male'),
#                ('niu', '123456', 'male'),
#                ('tang', '123456', 'male')))

# c.executemany('update user_tv set name =? where _id=?', (
#     ('小孙2', 2),
#     ('小孙3', 3),
#     ('小孙4', 4),
#     ('小孙5', 5),
#     ('小孙6', 6)
# ))
#
# print('修改的记录数量', c.rowcount)
#

# c.execute('''
#     create table user_tb(
#         user_id int primary  key auto_increment,
#         name varchar(255),
#         pass varchar(255),
#         gender varchar(255)
#     )
# ''')
#
# c.execute('''
#     create table order_tb(
#         order_id integer primary key auto_increment,
#         item_name varchar(255),
#         item_price double,
#         item_number double,
#         user_id int,
#         foreign  key(user_id) references user_tb(user_id)
#     )
# ''')

# c.execute('insert into user_tb values (null , %s, %s, %s)', ('孫悟空', '123456', 'male'))

# c.execute('insert into order_tb values (null , %s, %s, %s, %s)', ('鼠標', '34.2', '3', 3))
# conn.autocommit = True
c.executemany('insert into user_tb values (null , %s, %s, %s)',
          (
              ('sun', '123456', 'male'),
              ('bai', '123456', 'male'),
              ('zhu', '123456', 'male'),
              ('niu', '123456', 'male'),
              ('tang', '123456', 'male')
          ))

# conn.commit()

c.close()
conn.close()