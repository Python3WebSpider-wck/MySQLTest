import pymysql


id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root',
                     password='jojo123456', port=3306, db='spider')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
    print('Insert successfully')
except:
    db.rollback()
db.close()
