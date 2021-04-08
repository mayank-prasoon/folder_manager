import sqlite3
import os
import uuid
from datetime import datetime, date

database_path = os.getenv('USERPROFILE') + str('/documents')


class DatabaseManager:
    """ this build the database in document folder """

    def __init__(self):
        os.chdir(database_path)
        try:
            os.mkdir('Creative Manager')
        except:
            pass

        conn = sqlite3.connect(str(database_path) +
                               '/Creative Manager/' + "database.db")

        conn.cursor().execute("""CREATE TABLE IF NOT EXISTS "folder_path" (
            "id"	INTEGER NOT NULL UNIQUE,
            "project"	TEXT NOT NULL,
            "type"	TEXT NOT NULL,
            "path"	TEXT NOT NULL UNIQUE,
            "UId"	INTEGER NOT NULL UNIQUE,
            "date"	TEXT NOT NULL,
            "timespend"	TEXT,
            PRIMARY KEY("id" AUTOINCREMENT)
        )
            """)

        conn.commit()
        conn.close()

    def add_path(self, name, cat, path):
        """ create new project """
        Uid = uuid.uuid4()
        date = str(datetime.now().strftime("%B %d, %Y %H:%M:%S"))
        conn = sqlite3.connect(str(database_path) +
                               '/Creative Manager/' + "database.db")
        conn.cursor().execute("INSERT INTO 'folder_path' (project, type, path, Uid, date) VALUES (?, ?, ?, ?, ?)",
                              (name, cat, path, str(Uid), date))

        conn.commit()
        conn.close()

        print('new project has been created')

    def search_path(self, name='', Pid='', cat='', path=''):
        conn = sqlite3.connect(str(database_path) +
                               '/Creative Manager/' + "database.db")
        conn.cursor().execute("SELECT * FROM 'folder_path' WHERE id=? OR project=? OR type=? OR path=?",
                              (Pid, name, cat, path))

        row = conn.cursor().fetchall()
        conn.close()
        return row

    def search_all(self):
        con = sqlite3.connect(str(database_path) +
                              '/Creative Manager/' + "database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM folder_path")
        con.commit()
        rows = cur.fetchall()
        con.close()
        return rows

    def delete_path(self, Pid='', path=''):
        conn = sqlite3.connect(str(database_path) +
                               '/Creative Manager/' + "database.db")
        conn.cursor().execute("DELETE FROM 'folder_path' WHERE id=? OR path=?",
                              (Pid, path))
        conn.commit()
        conn.close()
        print(Pid, path)
        print('data coresponding to the following has been deleted:')

    def add_time(self, Pid="", time=""):
        conn = sqlite3.connect(str(database_path) +
                               '/Creative Manager/' + "database.db")
        conn.cursor().execute("UPDATE folder_path SET timespend=" +
                              str(time) + " WHERE id=" + str(Pid))
        conn.commit()
        conn.close()
