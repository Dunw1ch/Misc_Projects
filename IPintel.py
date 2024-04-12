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
    "x-apikey": ""
    }

    response = requests.get(url, headers=headers)

    info = response.text

    obj = json.loads(info)
    json_formatted_str = json.dumps(obj, indent=0)

    print(json_formatted_str)


input('Press ENTER to exit')
