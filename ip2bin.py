#!/usr/bin/python3
import argparse 
import ipaddress
from sys import exit

parser = argparse.ArgumentParser(description='IP zu Binär form')
parser.add_argument('IP', metavar='IP', type=str, help=' 0.0.0.0')
args=parser.parse_args()


ergebnis = ""

try:
	ipaddress.ip_address(args.IP) # Checkt ob IPv4
	ip = args.IP.split(".")
except: 
	print("Fehler in der IP ? Angegbene IP : %s"% args.IP)
	exit(666)


for index,octet in enumerate(ip):
	ip[index] = bin(int(octet)).replace("0b", "") # IP -> Binär
	ip[index] = ip[index].zfill(8) # Auffüllen mit nullen bis 8 bit



for octet in ip:
	ergebnis = ergebnis + octet + "." # Formatiert string

ergebnis = ergebnis[:-1] # strippt den letzten überflüssigen -


print(ergebnis)
