import sqlite3

## Connect to sqlite3
connection = sqlite3.connect('student.db')

## create a ccursor record 
cursor = connection.cursor()

## create a table
table_info ="""
Create Table STUDENT(
NAME VARCHAR(300),
CLASS VARCHAR(300),
SECTION VARCHAR(25),
MARKS INT
);
"""

cursor.execute(table_info)

### Insert some more record
cursor.execute('''INSERT INTO STUDENT values('krish','Data Science','A',90)''');
cursor.execute('''INSERT INTO STUDENT values('Pawan','Data Science','A',90)''');
cursor.execute('''INSERT INTO STUDENT values('Vikash','Data Engineer','B',80)''');
cursor.execute('''INSERT INTO STUDENT values('Naik','DEVOps','C',70)''');


## Display all the record
print('The inserted records are')

data  =  cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

## Close the connection
connection.commit();
connection.close();
