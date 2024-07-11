import sqlite3
import io 

    

def databaseinsert(fio, description, photo):
    connection = sqlite3.connect(r'db.sqlite3')
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


    connection = sqlite3.connect(r'db.sqlite3')
    cursor = connection.cursor()
    sqlite_insert = """INSERT INTO records_violations (fio, description, photo) VALUES (?, ?, ?)"""
    data_tuple = (fio, description, photo)
    cursor.execute(sqlite_insert, data_tuple)
    cursor.execute('COMMIT')
    cursor.execute("""SELECT * from records_violations""")
    result = cursor.fetchone()
    try:
        print (result[2])
    except:
        print('database is empty')
    cursor.close()


def read_BLOB(surname):
    
    connection = sqlite3.connect(r'db.sqlite3')
    cursor = connection.cursor()
    fetch_blob = """SELECT * from records_violations WHERE fio=?"""
    find = '%'+ surname + '%'
    cursor.execute(fetch_blob,find,)
    record = cursor.fetchone()
    connection.close
    return record
