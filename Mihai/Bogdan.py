'''
Created on May 1, 2012

@author: mide765
'''
import SendKeys
import os
import sys
import os.path
import subprocess
from time import sleep
import speech

#Goes to movie path
SendKeys.SendKeys("""
    {LWIN}
    {PAUSE 1}
    E
    {PAUSE 1}
    ~
    {PAUSE 1}
    {BKSP}
    
    {PAUSE 1}
    C
    ~
    {PAUSE 1}
    {RIGHT}
    ~
    {PAUSE 1}
    dow
    ~
    {PAUSE 1}
    {DOWN}
    {PAUSE 1}
    {UP}
    {UP}
""")

#Goes one file down until it hears something

dire="F:\\downloads"

def callback(phrase, listener):
    global ok
    ok=1
    listener.stoplistening()
    return -1
listener = speech.listenforanything(callback)
ok=0
for x in os.walk(dire):
    c=0
    while listener.islistening():
        #text = raw_input("> ")
        c=c+1
        if c==7000000:
            break
        elif ok==1:
            #Open mails for a quick overview of them & New York Times
            SendKeys.SendKeys("""
            ~
            {RIGHT}
            ~
            """)
            
    if ok==0:
        SendKeys.SendKeys("""
        {DOWN}
        """)
    if ok==1:
        break