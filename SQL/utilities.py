import sqlite3
import os

class BuildDb:
    """
    Ensures the user has the right databases built

    """
    def __init__(self):
        if 'SpammerSpammer.db' not in os.listdir('SQL'):
            self.__make_db()


    def __make_db(self):
        conn=sqlite3.connect(os.path.join('SQL','SpammerSpammer.db'))
        c = conn.cursor()
        query='''
        CREATE TABLE "contact_info" (
            "name"	text NOT NULL UNIQUE,
            "phone_number"	text,
            "imessage"	text,
            "notes"	text,
            "Field5"	NUMERIC,
            PRIMARY KEY("name")
        );'''
        c.execute(query)
        conn.commit()


if __name__ == "__main__":
    print('TRY AGAIN lol')
