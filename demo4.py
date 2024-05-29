import pymysql

data = {
    'id': '20120003',
    'name': 'Jeery',
    'age': 22
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
db = pymysql.connect(host='localhost', user='root',
                     password='jojo123456', port=3306, db='spider')
cursor = db.cursor()
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(
#     table=table, keys=keys, values=values)
sql = f'INSERT INTO {table}({keys}) VALUES ({values})'
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except Exception as e:
    print('Failed', e)
    db.rollback()
db.close()
