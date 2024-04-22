#Object: create a program that has a user input an IP address, then shows them a visual of where their traffic flowed via path ping
#steps:
#	1. Create a GUI for user to input an IP address
#	2. Project1 will run a pathping of that IP
#	3. Project1 will then grabb all the IP addresses from the path and then get coordinates for those
#	4. output the coordinates on a world map, hopefull draw lines as well?

from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
import subprocess

ipaddr = input("enter an IP you would like to see the path to: ", )

print("is this the IP you would like to see the path to?", ipaddr)

confirm = input("y/n")

if confirm == ('n'):
    print("ok, try another")
elif confirm == ('y'):
    print("ok running pathping on:", ipaddr)
    result = subprocess.run(['pathping', '-n', ipaddr], capture_output=True, text=True, check=True)
    print(result.stdout)
