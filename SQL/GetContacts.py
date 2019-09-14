class GetContacts:

    def __init__(self):
        query = """SELECT * FROM contact_info"""
        conn=sqlite3.connect(os.path.join('SQL', 'SpammerSpammer.db'))
        c = conn.cursor()
        c.execute(query)
        self.contact_list = c.fetchall()
        c.close()
        self.__contact_hash()
        print(self.contacts)

    def __contact_hash(self):
        self.contacts = {}
        self.spammers = {}
        for name, number, imessage, notes, spammer in self.contact_list:
            self.contacts[name]={'name', name, 'number':number, 'imessage':imessage, 'notes':notes, 'spammer':spammer}
            if spammer == True:
                self.spammers[name]=self.contacts[name]

if __name__ == "__main__":
    GetContacts()
