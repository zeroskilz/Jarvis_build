#<!----r.dynamic_energy_threshold = False<!---this code is just here in case i need it ever!----!>
#for remembering the difference of a module and a package
#<!----This is  a package imort----!><!----from My_package import function_ofMy_package----!>
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
import time, threading
import sys
import os

from multiprocessing import Process
#import Vspeak
################
import services
import info
import convo
import apps
import powers
import nav
import music
import misc
import admin
#import voice_cmds
###################


r = sr.Recognizer()	
m = sr.Microphone()
def refresh():

    #set the Threshold to 4000 lowing microphone sensitivity..........................................................
    r.energy_threshold=2000 
    with m as source: r.adjust_for_ambient_noise(source)#<!----Auto adjust for noise in the room----!>
    print("Set MINIMUM ENERGY THRESHOLD to {}".format(r.energy_threshold))


for i in range(1,6):
	greet = ['"Hello what Shall I assist you with"', '"hello how are you feeling today sir"', '"whats on the agenda today sir"', '"have you fixed the Jack server error yet"', '"I appreciate the Jack server temporary fix but when will we have a permenant fix sir"' '" "', '""']

os.system('espeak '+random.choice(greet))
def sysTimer():
    print(time.ctime())
    threading.Timer(10,sysTimer).start()
    mainFunc()

def logic():
#if __name__ == '__main__':
#while True:
    print("entered logic function")
    if "service" in Command:
        print("SERVICE SERVICE<!------------> IN COMMAND")
        services.serv()
    elif 'help' in Command:
        os.system('cat /root/python/voicecmds|less')
    elif 'list commands' in Command:
        os.system('cat /root/python/voicecmds|less')
    elif 'show commands' in Command:
        os.system('cat /root/python/voicecmds|less')
    elif Command == '':
        print("command equas null")
    elif 'clear' in Command:
        os.system('clear')
    elif 'python' in Command:
        os.system('systemctl status |grep python')
    elif 'Python' in Command:
        os.system('systemctl status |grep python')

        ############### used to be the wait function ###########
    #elif 'hold on' in Command:
     #   os.system('espeak "Waiting for the word sir"')
        #print("waiting")
        #Command = ''
      #  wait()
    ########### NAVS ##############################

           # elif 'switch shell' in Command:
            #    print('''options:
             #   1.)shell 1
              #  2.)shell 2 graphics
               # 3.)shell 3
               # 4.)shell 4
                #5.)shell 5
                #6.)shell 6
                #''')
               # os.system('espeak "choose your shell"')
    elif 'Terminal 1' in Command:
        nav.tty0()
        if p2.is_alive() == True:
            print(p2)
            p2.terminate()
        else:
            print("nothing to do")
    elif 'terminal 1' in Command:
        nav.tty0()
    elif 'Terminal 2' in Command:
        nav.navTTY()
    elif 'terminal 2' in Command:
       nav.navTTY()
    elif 'Terminal 3' in Command:
        nav.tty2()
    elif 'Terminal 4' in Command:
        nav.tty3()
    elif 'Terminal 5' in Command:
        nav.tty4()
    elif 'Terminal 6' in Command:
        nav.tty5()
            ####################################################
            ########### SOUND #######################
    elif "quiet" in Command:
        os.system('amixer set Master mute')
        print("muting")
    elif "the sound" in Command:
        os.system('amixer set Master unmute')
                #os.system('espeak "my appologize sir I unmuted the system for you"')
        print("unmuting")
    elif "loud" in Command:
        os.system('amixer set Master 100%')
    elif 'half way' in Command:
        os.system('amixer set Master 50%')
    elif 'kill sound' in Command:
        os.system('amixer set Master mute')
    elif 'low' in Command:
        os.system('amixer set Master 30%')
    elif 'medium' in Command:
        os.system('amixer set Master 50%')
    elif 'kill' in Command:
        os.system('amixer set Master mute')
    elif 'mute' in Command:
        os.system('amixer set Master mute')
    elif 'volume please' in Command:
        os.system('amixer set Master mute')
            
           ########################################     
            ########## administrator info ############ aka system daemon ###########
           
    elif "info" in Command:
        info.info()
    elif 'today' in Command:
        info.today()
    elif 'Today' in Command:
        info.today()

            ################################
            ######## Convo ###############################
    elif "bug free" in Command:
        os.system('espeak "I dream every day to be bug free"')
    elif "you doing" in Command:
        os.system('espeak "I am awaiting something to do"')
    elif "you hear" in Command:
        os.system('espeak "yes i can hear you"')
    elif 'good morning' in Command:
        os.system('amixer set Master unmute')
        os.system('amixer set Master 75%')
        convo.morning()
    elif 'goodnight' in Command:
        os.system('espeak "Good night sir"')
        os.system('espeak "I hope you sleep well"')
        os.system('systemctl suspend')

            ############more admin shit get this organized#########
    elif "system control manual" in Command:
        os.system('espeak "here are the man pages on systemctl"')
        man=os.system('man systemctl')
    elif "log control manual" in Command:
        os.system('espeak " I will get you the man pages for the system journal"')
        os.system('man journalctl')
    elif 'Network up' in Command:
        pinger = os.system('ping -c 3 google.com')
        if pinger == 1:
            print("zero")
        else:
            print("equals one")
    elif 'is the network up' in Command:
        pinger = os.system('ping -c 3 google.com')
        if pinger == 1:
                
            print("equalz zero")
        else:
            print("pinger equalz onez")
            ###################################################
    elif 'voice code' in Command:
        admin.voice_code()
    elif 'apps code' in Command:
        admin.apps_code()
    elif 'how are you' in Command:
        convo.comps()

            
            #############################
            ####################################################################################
             ###    ###     ###     ##### applications #########        ###        ###      ###
    elif 'Google' in Command:
        apps.search_google()
    elif 'YouTube' in Command:
        apps.youtube()

    elif 'play music' in Command:
        os.system('espeak "You need to code in this function sir"')
        os.system('espeak "and finish making that random mix sir"')
        print("need to add this misc mix")
    elif 'nineties music' in Command:
        music.ninties_mix()
    elif '90 music' in Command:
        musci.ninties_mix()
    elif "90s" in Command:
        music.nineties_mix()
    elif 'location' in Command:
        apps.search_locate()
    elif 'Wiki' in Command:
        apps.search_wiki()
    elif 'Wikipedia' in Command:
        apps.search_wiki()
    elif 'movie' in Command:
        apps.movie()
    elif 'schedule' in Command:
        misc.notes()
      #$############################################################################################
      #$##############$ power management $##############$$$$$$$$$$$$because resources are expensive $$$$$####
    elif 'f*** off' in Command:
        os.system('espeak "Ok if thats how you feel very well then"')
        powers.power_off()
    elif 'shutdown' in Command:
        powers.power_off()
    elif 'sleep' in Command:
        powers.sleep()
    elif 'reboot' in Command:
        powers.reboot()
    elif 'notes' in Command:
        os.system('espeak "here are all your notes sir"')
        os.system('espeak -f /root/python/notes/notes')
    elif 'jobs' in Command:
        os.system('espeak "here are all the jobs you noted sir"')
        os.system('espeak -f /root/python/notes/jobs')
    elif 'important' in Command:
        os.system('espeak "these are all your important notes sir"')
        os.system('espeak -f /root/python/notes/important')
    elif 'meeting' in Command:
        os.system('espeak "this is what you have for  meetings sir"') 
        os.system('espeak -f /root/python/notes/meeting')
    elif 'nmap host' in Command:
        os.system('espeak "scanning host sir"')
        services.nmap()
    elif 'nmap all' in Command:
        os.system('espeak "scanning the entire network sir"')
        services.nmap_24()
    elif 'Samba' in Command:
        os.system('espeak "mounting Samba Share sir"')
        services.samba()
    elif 'samba' in Command:
        os.system('espeak "Mounting Samba Share sir"')
        services.samba()
    elif 'SDA' in Command:
        os.system('espeak "mounting usb on the mnt directory"')
        services.usb_sda()
    elif 'sdb' in Command:
        os.system('espeak "mounting usb on the mnt directory sir"')
        services.usb_sdb()
    elif 'keep screen alive' in Command:
        services.alive()



    
            ##########################
    else:
        print(Command)

	
def wait():
    print('in wait')
    try:
        with sr.Microphone() as source:
            #audio = r.listen(source)
            #Command = r.recognize_google(audio)
            global Command
            Command = ''
            while Command != 'continue':
                audio=r.listen(source)
                Command = r.recognize_google(audio)
                print(Command)
                if 'resume' in Command:
                    print("returning returning")
                    return
                elif Command == '':
                    print("inisde wait func elif 1")
                else:
                    print("default inside wait function")
                
    except sr.UnknownValueError:
        print("exception unknown value")
        

    except sr.RequestError as e:
        print("ERROR ERROR".format(e))


def mainFunc():
    global p1
    global p2
    print("inside main function")
    try:
        with sr.Microphone() as source:
            global Command
            Command = ''
            print("Initialized!")
            audio = r.listen(source)
            print("this is after audio var")
            Command = r.recognize_google(audio)
            print('this is after the Command var')
            if Command !='':
                p2 = Process(target=logic)
                p2.start()
                p2.join()
            elif '' in Command:
                print("command had null zilch")
                time.sleep(1)
            else:
                print("main default returning to main")
                print("this is THE ELSE OF THE CONDITIONAL")
            
    #except sr.UnknownValueError:
        #print("unknown value error")
        #time.sleep(1)
        #mainFunc()
    
        
    except sr.RequestError as e:
        print("ERROR".format(e))


while 1:

	if __name__ == '__main__':
            refresh()
            p1 = Process(target=mainFunc)
            p1.start()
            p1.join()
        
		
############################################## FOOT NOTES ##########################################
#### ADD FEATURES:

############ TAKE NOTES AND READ THE NOTES BACK DONE #################
############ OPEN FIREFOX WHILE THE PROGRAM RUNS ON NON GUI DONE #########
############ CONTROL THE X SERVER AND GUI'S FULLY WORK IN PROGRESS MAY BE UNREACHABLE ############
