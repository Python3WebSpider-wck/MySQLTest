import pymysql

data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 22
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
db = pymysql.connect(host='localhost', user='root',
                     password='jojo123456', port=3306, db='spider')
cursor = db.cursor()

# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(
#     table=table, keys=keys, values=values)
# update = ','.join(["{key} = %s".format(key=key) for key in data])
# duplicate adj.完全一样的，复制的
sql = f'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '
update = ','.join([f'{key} = %s' for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except Exception as e:
    print('Failed', e)
    db.rollback()
db.close()
