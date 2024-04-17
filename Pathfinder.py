#Object: create a program that has a user input an IP address, then shows them a visual of where their traffic flowed via path ping
#steps:
#	1. Create a GUI for user to input an IP address
#	2. Project1 will run a pathping of that IP
#	3. Project1 will then grabb all the IP addresses from the path and then get coordinates for those
#	4. output the coordinates on a world map, hopefull draw lines as well?

import tkinter as tk
import socket
import requests
from tkinter.simpledialog import askstring, askinteger
from tkinter.messagebox import showerror
import pexpect
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

window = tk.tk()
greeting = tk.label(ip_add = input("Enter IP: "))
greeting.pack()
greeting.mainloop()
print("is this the IP you would like to search?", ip_add)
confirm = input("y/n")

if confirm == ('n'):
    print("ok, try another")
elif confirm == ('y'):
    print("ok running pathping on:", ip_add)

child = pexpect.spawn('pathping -c 5 1.1.1.1')
while 1:
        line = child.readline()
        if not line: break
        print line,


'''
window = tk.Tk()

# Function to get the user input and print it
def get_input():
    ip_address = ip_entry.get()
    print("Is this the IP you would like to search?", ip_address)
    confirm = input("y/n")

# Label widget to prompt the user
label = tk.Label(window, text="Enter IP:")
label.pack()

# Entry widget to get the input
ip_entry = tk.Entry(window)
ip_entry.pack()

# Button to submit the input
submit_button = tk.Button(window, text="Submit", command=get_input)
submit_button.pack()

# Run the main event loop
window.mainloop()
'''
