'''
Created on May 1, 2012

@author: Bogdan
'''
import speech
import sys
import webbrowser
import os
#speech.say("STAR WARS IS A LIE")

def callback(phrase, listener):
    global ok
    ok=1
    handle = webbrowser.get()
    handle.open_new_tab('http://www.google.com')
    listener.stoplistening()
    return -1

print "Anything you type, speech will say back."
print "Anything you say, speech will print out."
print "Say or type 'turn off' to quit."
print
ok=0
listener = speech.listenforanything(callback)
text=""
while listener.islistening():
    #text = raw_input("> ")
    if text == "turn off":
        listener.stoplistening()
        break
    else:
        speech.say(text)
    
if __name__ == '__main__':
    pass