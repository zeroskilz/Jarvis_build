#!/usr/local/bin/python

import speech_recognition as sr
#from time import gmtime ,strftime
#from datetime import date
from gtts import gTTS
import re, urllib
#import webbrowser
import subprocess
#import datetime
#import calendar
import random
#import date
import time
import sys
import os

r = sr.Recognizer()							
#m = sr.Microphone()
#set the Threshold to 4000 lowing microphone sensitivity..........................................................
r.energy_threshold=4000 
#with m as source: r.adjust_for_ambient_noise(source)#<!----Auto adjust for noise in the room----!>
print("Set MINIMUM ENERGY THRESHOLD to {}".format(r.energy_threshold))
def today():
    os.system('echo `date` >> /root/python/date')
    os.system('espeak -f /root/python/date')

def info():
    os.system('espeak "here are your options"')
    print(''' options are:
    1.)system status [status] 
    2.)unit files
    3.) boot info
    ''')
    os.system('espeak "system status"')
    os.system('espeak "unit files"')
    os.system('espeak "boot info"')
    try:
        with sr.Microphone() as source:
            print("Microphone is Initialized!")
            #audio = r.listen(source)
           # command = r.recognize_google(audio)
            while True:
                command=''
                audio=r.listen(source)
                command=r.recognize_google(audio)

                print("inside first while")
                if 'status' in command:
                    os.system('espeak "here is the info on your system status"')
                    os.system('systemctl status')
                elif 'unit files' in command:
                    os.system('espeak "here are your options on unit files"')
                    print('''options for viewing units :
                    1.)all
                    2.)service
                    3.)target
                    4.)scope
                    5.)slice
                    ''')
                    os.system('espeak -g 40 "All service target scope and slice"')
                    print("waiting for exit command")
                    while command !='exit':
                        print("inside second while")
                        audio=r.listen(source)
                        command=r.recognize_google(audio)
                        if 'exit' in command:
                            return
                        elif 'all' in command:
                            os.system('systemctl list-unit-files')
                        elif 'services' in command:
                            os.system('systemctl list-unit-files --type=service')
                        elif 'target' in command:
                            os.system('systemctl list-unit-files --type=target')
                        elif 'scope' in command:
                            os.system('systemctl list-unit-files --type=scope')
                        elif 'slice' in command:
                            os.system('systemctl list-unit-files --type=slice')


                elif 'boot info' in command:
                    print('''options:
                    1.)current
                    2.)previous
                    ''')
                    os.system('espeak "would you like the error reports for the current or previous boot sir"')
                    audio = r.listen(source)
                    boot_cmd=r.recognize_google(audio)
                    if 'current' in boot_cmd:
                        os.system('journalctl -p err -b')
                    elif 'previous' in boot_cmd:
                        os.system('journalctl -p err -b -1')
                elif 'quit' in command:
                    return
                elif 'exit' in command:
                    return

    except sr.UnknownValueError: 
       # os.system('espeak "there is an unknown value in the system"')
       # os.system('espeak "Sir i think you should get that fixed"')
        info()
    except sr.RequestError as e:
        #os.system('espeak "there has been an exception sir"')
        print("ERROR".format(e))
        info()

