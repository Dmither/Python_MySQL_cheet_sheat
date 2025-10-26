import mysql.connector as connector

with connector.connect(
    host='localhost',
    user='root',
    password='111111',
    database='academy'
) as connection:

    cursor = connection.cursor()

    sql = 'INSERT INTO people (name, age) VALUES (%s, %s)'
    values = [('Sam', 43), ('Anna', 28)]
    cursor.executemany(sql, values)
    print(cursor.lastrowid)  # return ID of last inserted row
    print(cursor.rowcount)