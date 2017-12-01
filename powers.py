#!/usr/local/bin/python
import os
def exit():
    exit 

def power_off():
    os.system('espeak "If thats how you feel sir"')
    #choice=input("enter shutoff passwd")
    #choice = 'rbpasswd'
    #if choice == 'rbpasswd':
    os.system('espeak "system will now be powered off goodnight"')
    os.system('systemctl poweroff')
    #else:
       # os.system('espeak "you have input a faulty password"')

def reboot():
    os.system('espeak "Sir are you sure you want to go down for a reboot"')
    #choice = input("enter password for reboot")
    #choice = 'rbpasswd'
    #if choice == 'rbpasswd':
    os.system('espeak "going down for a reboot"')
    os.system('reboot')
    #else:
       # os.system('espeak "you entered the wrong password"')

def sleep():
    os.system('espeak "we havent added the sleep function yet sir"')

