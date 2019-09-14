import sqlite3
import os

def add_number():
	"""
	allows adding a number to existing database
	"""
	print('enter name')
	name=('name',input())
	print('enter number [leave blank if imessage')
	number=('phone_number',input())
	print('enter imessage [leave blank if phonenum')
	imessage=('imessage',input())
	print('enter notes if any')
	notes=('notes',input())
	print('spammer? [1 or leave blank]')
	spammer=('spammer', input())
	#format to insert to SQL
	SQL_col = []
	SQL_val = []
	for col, val in [name,number,imessage,notes, spammer]:
		if len(val) > 0:
			SQL_col.append(col)
			SQL_val.append(val)
	query = "INSERT INTO contact_info ( %s ) VALUES (%s)" %( (', ').join(SQL_col), (',').join("?"*len(SQL_val)))
	print(query)
	conn = sqlite3.connect(os.path.join('SQL', 'SpammerSpammer.db'))
	c =  conn.cursor()
	c.execute(query, SQL_val)
	conn.commit()
	c.close()

if __name__ == "__main__":
    add_number() 
