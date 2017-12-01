#!/usr/local/bin/python
import speech_recognition as sr
import re, urllib
import webbrowser
import subprocess
import datetime
import calendar
import random
import time
import sys
import os
import wikipedia
r = sr.Recognizer()							
m = sr.Microphone()
#set the Threshold to 4000 lowing microphone sensitivity..........................................................
r.energy_threshold=4000 
with m as source: r.adjust_for_ambient_noise(source)#<!----Auto adjust for noise in the room----!>
print("Set MINIMUM ENERGY THRESHOLD to {}".format(r.energy_threshold))



def search_google():
    os.system('espeak "I will need to know the type of content you wish for me to retrieve"')
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            Command = r.recognize_google(audio)
            os.system('espeak "I am retrieving info about%s"'%Command)
            os.system("DISPLAY=:0 firefox www.google.com/#q='%s'"%Command+" & exit")
    
           # webbrowser.open('https://google.com/#q=%s'%Command, new=2)
    except sr.UnknownValueError:
        search_google()

    except sr.RequestError as e:
        print("ERROR".format(e))
        search_google()



def search_locate():
    os.system('espeak "What Location would you like me to pin point"')
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            Command = r.recognize_google(audio)
            os.system('espeak "I bring to you %s"'%Command)
            os.system("DISPLAY=:0 firefox www.google.com/maps/place/%s"%Command+" & exit")
            print(Command)
            
#            webbrowser.open('https://www.google.com/maps/place/%s'%Command, new=2)
    except sr.UnknownValueError: 
        search_locate()
    except sr.RequestError as e:
        print("ERROR".format(e))
        search_locate()


def search_wiki():
    os.system('espeak "What data do you want me to get you Sir"')
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            Command = r.recognize_google(audio)
            #os.system('espeak "Im On it i will get you the info"i')
            content = wikipedia.summary(Command)
            content = re.sub('[(){}<>]', "", content)
            f=open('/root/python/web/wiki', 'w')
            f.write(content)
            f.close()
            print(content)
            os.system('espeak -f /root/python/web/wiki') 
            print("returning to main")
            
#           
    except sr.UnknownValueError: 
        search_wiki()

    except sr.RequestError as e:
        print("ERROR".format(e))
        search_wiki()



def search_web():
    os.system('espeak "Ok what website would you like to visit?"')
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            Command = r.recognize_google(audio)
            if 'stack overflow' in Command:
                os.system('espeak "Ok I am taking you to%s"'%Command)
                webbrowser.open('https://www.stackoverflow.com/', new=2)
            else:
                os.system('espeak "Ok I am taking you to%s"'%Command)
                webbrowser.open('https://www.%s'%Command+'.com', new=2)
                print('This is for Seeing the way the voice rec software returns the website string....%s'% Command)
    except sr.UnknownValueError:
        search_web()

    except sr.RequestError as e:
        print("ERROR".format(e))
        search_web()

def youtube():
    os.system('espeak "What do you want me to Search for you on youtube"')
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            Command = r.recognize_google(audio)
            os.system('espeak "Nice Choice .....I will get%s'%Command+'for you Jargon"')
            os.system("DISPLAY=:0 firefox www.youtube.com/results?search_query='%s'" %Command+" & exit")
        
            #webbrowser.open('https://www.youtube.com/results?search_query='+Command, new=2) 

    except sr.UnknownValueError:
        youtube()

    except sr.RequestError as e:
        print("ERROR".format(e))
        youtube()



def movie():
    os.system('DISPLAY=:0 firefox www.alluc.ee & exit')

