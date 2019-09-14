import subprocess

from SQL.utilities import GetNumbers
#todo should import to db and make sure all is ok there

class Message():

    def __init__():
        self.__get_numbers()
	    pass	

    def send_imessage(self,content,person=None,number=None)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
        subprocess.call(["osascript", "SendImessage.applescript", '"%s"'%(number), '"%s"'%(content)])

