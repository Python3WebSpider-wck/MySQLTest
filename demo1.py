import pymysql

db = pymysql.connect(host='localhost', user='root', password='jojo123456', port=3306)
# n.光标，游标，指针
cursor = db.cursor()

cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)

cursor.execute("CREATE DATABASE spider DEFAULT CHARACTER SET utf8mb4")
db.close()
