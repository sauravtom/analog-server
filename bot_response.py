import os

def response():
    return "Hello"

def sentiment(msg):
    import subprocess
    output = subprocess.check_output("curl -d \"text="+str(msg)+"\" http://text-processing.com/api/sentiment/", shell=True)
    print output
    ans = output.split()
    resp = ans[-1].split("\"")[1]

    if resp == 'neg':
        return 'Oh! That\'s sad'
    else:
        return 'That\'s awesome!!'

#print sentiment()