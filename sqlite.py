import sqlite3

## connect to sqlite
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record. create table
cursor=connection.cursor()

## create the table
table_info="""
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Abhishek','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Anu','Data Science','B',95)''')
cursor.execute('''Insert Into STUDENT values('Aditi','Gen AI','A',100)''')
cursor.execute('''Insert Into STUDENT values('Shruti','DEVOPS','A',65)''')
cursor.execute('''Insert Into STUDENT values('Kishan','DEVOPS','A',45)''')

## Displat all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
    