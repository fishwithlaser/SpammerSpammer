import subprocess

class Message():
    """
    determines if imessage or sms and sends
    """
    def __init__():
        self.__assign contacts() #self.contacts and self.spammers now hashmaps with 'name', 'number', 'imessage' and 'notes'

    def __assign_contacts():
        from SQL.GetContacts import GetContacts
        Contacts=GetContacts()
        self.contacts = Contacts.contacts
        self.spammers = Contacts.spammers

    def send_imessage(self,content,person=None,number=None)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
        subprocess.call(["osascript", "SendImessage.applescript", '"%s"'%(number), '"%s"'%(content)])



