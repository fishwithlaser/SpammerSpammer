import subprocess

def send_targeted_message(message, method):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if 'number' in method.keys():
        subprocess.call(["osascript", "SendSMS.applescript", '"%s"' % method['number'], '"%s"' % (message)])
    elif 'imessage in method.keys()':
        subprocess.call(["osascript", "SendImessage.applescript", '"%s"' % method['imessage'], '"%s"' % (message)])
