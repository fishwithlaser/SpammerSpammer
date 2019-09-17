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
        #creates content table
        query='''
        CREATE TABLE "message_content" (
            "machine_generated" bit,
            "recieved" bit,
            "owner" varchar(255),
            "theme" varchar(255),
            "content" text
        )
        
        '''
        c.execute(query)
        # creates contact table
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

def open_connection():
    """opens db if configured in this way __^ """
   conn = sqlite3.connect(os.path.join('SQL','SpammerSpammer.db'))
   c = conn.cursor()
   return conn, c



if __name__ == "__main__":
    print('TRY AGAIN lol - thomas didnt actually write anything here..')
