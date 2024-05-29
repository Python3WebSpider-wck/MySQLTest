import pymysql

# 创建数据库后，在连接时需要额外指定一个参数db
db = pymysql.connect(host='localhost', user='root', password='jojo123456', port=3306, db='spider')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
db.close()
