"""
A bit of fun messing with the Shodan API, outputs a random ransom letter detected by Shodan.
"""
from shodan import Shodan
from shodan.cli.helpers import get_api_key

api = Shodan(get_api_key())

#incredibly important to add a limit to not overdue credit limit of 10k results a month
limit = 1
counter = 0


for banner in api.search_cursor('has_screenshot:true encrypted attention'):
    print(banner['data'])

    counter += 1
    if counter >= limit:
        break
