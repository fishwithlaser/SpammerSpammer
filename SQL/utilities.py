import sqlite3
import os



class buildDb:

    def __init__():
        if 'SpammerSpammer.db' not in os.listdir('SQL'):
            __make_db()


    def __make_db():
        conn=sqlite3.connect('SpammerSpammer.db')
        c = conn.cursor()
        query='''CREATE TABLE numbers
                 (name text, phonenumber text, imessage text, notes text)'''
        c.execute(query)
        conn.commit()
        c.close()

