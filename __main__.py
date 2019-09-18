import subprocess
""" below seems to work
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
subprocess.call(["osascript", "SendImessage.applescript", '"+12047201366"', '"TESTING :) "'])
"""