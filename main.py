#!/usr/local/bin/python
import os
import services
import info
### old list to call functions from found a better way making modules for adding to########
#services = {'start network': [netctl], 'ssh': [ssh]}
#info = {'status': [status], 'unit_files': [unit_files], 'boot_info': [boot_info]}
#types = raw_input("what may i help you with")
############ issue command to accept user_input######################
print("options:")
print ("1.)services")
print ("2.)info")


def main():


   # for ret in ai:
    #    ret()
    command=input("what about?:")
    if 'services' in command:
        services.serv()
    elif 'info'in command:
        info.info()

#########old###########
#if 'services' in types:
   # execute(services[command])
#elif 'info' in types:
   # ecute(info[command])

#### foot notes####
#add the ability to easily store code into the scripts memory and have the program ask if it should be conditional or not if so then use arguments like so to add conditionals for the command and how many different conditions so all you may need to do is type new command and then another option will come up to add the arguments for the conditionals as so 3<!amount of conditionals ie if elif elif-->  matching will be argument one of if in command for cond 1 ie input as so
#3 keyword0 keyword1 keyword2-->

while 1: 
    if __name__ == '__main__':
        main()
