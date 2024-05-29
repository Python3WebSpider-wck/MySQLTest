import pymysql

table = 'students'
condition = 'age > 21'

db = pymysql.connect(host='localhost', user='root', password='jojo123456', port=3306, db='spider')
cursor = db.cursor()
# sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
sql = f'DELETE FROM {table} WHERE {condition}'
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
