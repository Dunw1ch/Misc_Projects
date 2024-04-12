#documentation for this library: https://pypi.org/project/requests-tor/

from requests_tor import RequestsTor

requests = RequestsTor(tor_ports=(9050,), tor_cports=9051)

url = #url here
r = requests.get(url)

print(r.text)