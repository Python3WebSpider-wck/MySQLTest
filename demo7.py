import pymysql

db = pymysql.connect(host='localhost', user='root', password='jojo123456', port=3306, db='spider')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')

sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
