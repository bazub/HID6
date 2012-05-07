'''
Created on May 1, 2012

@author: mide765
'''
import webbrowser
import SendKeys
import os
import os.path
import subprocess
from time import sleep

#Make it say: 'Are you working?'. If it hears something it opens the mails and the notepad. If not, music.
import speech
speech.say("Hey Mihai, are you working?")
def callback(phrase, listener):
    global ok
    ok=1
    listener.stoplistening()
    return -1
ok=0
c=0
listener = speech.listenforanything(callback)
text=""
while listener.islistening():
    #text = raw_input("> ")
    c=c+1
    if c==10000000:
        break
    elif ok==1:
        #Open mails for a quick overview of them & New York Times
        handle = webbrowser.get()
        handle.open_new_tab('http://mail.google.com')
        sleep(5)
        handle.open_new_tab('http://mail.yahoo.com')
        sleep(5)
        handle.open_new_tab('http://nyt.com')

#Open & Play Winamp
if ok==0:
    print c
    wamp_exe = r'C:\Program Files (x86)\Winamp\winamp.exe'
    assert os.path.exists(wamp_exe)
    url = "http://80.86.106.35:80"
    child = subprocess.Popen( (wamp_exe, url), executable = wamp_exe)

sleep(10)