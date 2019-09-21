
class AddMessage:

    def __init__(self):
        print('nothing here ...')

    def __add_message(self, content, **kwargs):
        from SQL.utilities import open_connection
        sql_cols=['content']
        sql_vals=[ content ]
        for item in ['machine_generated', 'recieved', 'owner','theme']:
            if item in ['machine_generated', 'recieved']:
                assert len(kwargs[item]) in [1,0]
            if item in kwargs.keys():
                sql_cols.append(item)
                sql_vals.append(kwargs[item])
        query = "INSERT INTO message_content (%s) VALUES (%s)"%(','.join(sql_cols) ,'?'*len(sql_vals))
        con, c = open_connection()
        c.execute(query, sql_vals)
        c.commit()
        conn.close()

    @property
    def message_add_add():
        import clipboard
        accepted='n'
        while accepted != 'y':
            message = clipboard.paste()
            print(message+'\n\n\n input the above message (stolen from your clipboard)? if so input y')
            accepted=input()
        obj = AddMessage
        AddMessage.__add_message()
