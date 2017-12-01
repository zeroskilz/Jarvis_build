#!/usr/local/bin/python
import os
def ssh_serv():
    os.system('systemctl start sshd')
    print('ssh started')

def wifi():
    os.system('netctl start wlo1-Randreano')
    os.system('wifi-menu wpl0s20u2')
    os.system('wifi-menu wlp0s20u1')
    print("Connected to wireless network")

def usb_sda():
    print("mounting usb on /mnt")
    os.system('mount /dev/sda1 /mnt')
    
    
def usb_sdb():
    print('mounting usb on /android')
    os.system('mount /dev/sdb1 /android')

def samba():
    
    print("mounting network share")
    os.system(' cd /root/bash && ./samba.sh & exit')
    #os.system("mount -t cifs 192.168.1.1\\sda1 /samba -o rw")
    print("mounted the share")

def nmap():
    print("scaning network")
    os.system('nmap 192.168.1.1 > nmap_host')
    os.system('cat nmap_host|less')

def nmap_24():
    print("scanning all 255 addresses on the nertwork")
    os.system('nmap 192.168.1.1/24 > nmap')
    os.system('cat nmap |less')
def alive():
    os.system('xset s off -dpms')
    print('KEEPING SCREEN ALIVE')



#################### FOOT NOTES MAKE SCRIPT TO TRY TO CONNECT TO EVERY SAMBA SHARE ON THE NETWORK UNTIL IT RETURNS TRUE ###############
