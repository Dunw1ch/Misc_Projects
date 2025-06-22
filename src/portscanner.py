from scapy.all import *
import ipaddress

ports = [21,22,25,53,80,443,445,8080,8443]

def SynScan(host):
    ans, unans = sr(
        IP(dst=host)/
        TCP(sport=33333,dport=ports,flags="S")
        ,timeout=2, verbose=0)
    print("open ports at %s:" % host)
    for(s, r,) in ans:
        if s[TCP].dport == r[TCP].sport and r[TCP].flags=="SA":
            print(s[TCP].dport)

def DNSScan (host):
    ans,unans = sr(
        IP(dst=host)/
        UDP(dport=53)/
        DNS(rd=1, qd=DNSQR(qname="google.com"))
        ,timeout=2, verbose=0)
    if ans and ans[UDP]:
        print("DNS server at %s"%host)

def new_func():
    return 0

host = input("enter an IP address: ")
try:
    ipaddress.ip_address(host)
except:
    print("Invalid address")
    exit(-1)

SynScan(host)
DNSScan(host)