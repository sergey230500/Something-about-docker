import sqlite3
import io 
from datetime import datetime
    

def databaseinsert(fio, description, photo):
    connection = sqlite3.connect('/pythonbot/database/db.sqlite3')


    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records_violations (
            id INTEGER PRIMARY KEY,
            date TEXT,
            FIO TEXT,
            DESCRIPTION TEXT,
            PHOTO BLOB
        );""")
    
    image = io.BytesIO(photo)
    connection.commit()
    connection.close()


    connection = sqlite3.connect('/pythonbot/database/db.sqlite3')
    cursor = connection.cursor()
    print('Подключение успешно')
    date = datetime.now().isoformat()
    sqlite_insert = """INSERT INTO records_violations (date, fio, description, photo) VALUES (?, ?, ?, ?)"""
    data_tuple = (date, fio, description, photo)
    cursor.execute(sqlite_insert, data_tuple)
    cursor.execute('COMMIT')
    print('Запись внесена')
    cursor.execute("""SELECT * from records_violations""")
    result = cursor.fetchone()
    try:
        print (result[2])
    except:
        print('database is empty')
    cursor.close()


def read_BLOB(surname):
    
    connection = sqlite3.connect('/pythonbot/database/db.sqlite3')
    cursor = connection.cursor()
    fetch_blob = """SELECT * from records_violations WHERE fio=?"""
    find = '%'+ surname + '%'
    cursor.execute(fetch_blob,find,)
    record = cursor.fetchone()
    connection.close
    return record
