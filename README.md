# Python MySQL cheat sheet

Installation:

```bash
pip install mysql-connector-python
```

Import and connection:

```python
import mysql.connector as connector

with connector.connect(
    host='localhost',
    user='user',
    password='password',
    database='my_db' # optional
) as connection:
    pass
```

Row queries:

```python
cursor = connection.cursor()
cursor.execute('CREATE DATABASE my_db')
```

Commit and placeholders (prevent SQL injections):

```python
cursor.execute('INSERT INTO my_tbl (name, age) VALUES (%s, %s)', ('John', 32))
connection.commit()
```

Executemany, lastrowid and rowcount:

```python
sql = 'INSERT INTO my_tbl (name, age) VALUES (%s, %s)'
values = [('Sam', 43), ('Anna', 28)]
cursor.executemany(sql, values)
connection.commit()
print(cursor.lastrowid)  # return ID of last inserted row
print(cursor.rowcount)   # return how many rows inserted
```

Fetch:

```python
cursor.execute('select * from people')
print(cursor.fetchone())   # get next one
print(cursor.fetchmany(2)) # get next many
print(cursor.fetchall())   # get all the left
```

