import requests
import json


#look at adding pretty print for the JSON file parser

IP = input("Welcome to the Virustotal API! type an IP address to get started:")

print("thanks, your IP is ", IP)
x = input("are you ready to search? y/n")

if x == "n":
    print("okay lets try another")
    
if x == "y":
    url = "https://www.virustotal.com/api/v3/ip_addresses/"+IP

    headers = {
    "accept": "application/json",
    #add API key below
    "x-apikey": "dd6921978ef32e2e9fe2494330f3b2061ffd65c6527740911d10bb06b90d1a6b"
    }

    response = requests.get(url, headers=headers)

    info = response.text

    obj = json.loads(info)
    json_formatted_str = json.dumps(obj, indent=0)

    f = open('VirusTotalreport.txt', 'w')
    f.write(json_formatted_str)
    f.close()

input('Press ENTER to exit')
