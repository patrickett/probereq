#!/usr/bin/env python2
from scapy.all import *
import sys
from os import geteuid
from sys import exit as sys_exit
from time import gmtime, strftime
from manuf import manuf #wireshark oui
import argparse

parser = argparse.ArgumentParser(description='Demo')
parser.add_argument('--interface', '-i',required=True,help='Name of wireless interface in monitor mode' )
args = parser.parse_args()
iname = args.interface
f = open('probes.txt', 'a')
os.system('clear')
broad = raw_input("Do you want broadcast probes? (Does not produce SSID) [Y/n]: ")
yes = {'yes','y', 'ye', ''}
no = {'no','n'}

if broad in yes :
    print("Sniffing all probe requests...")
    def proc(p):
        if ( p.haslayer(Dot11ProbeReq) ):
                mac=re.sub('','',p.addr2)
                ssid=p[Dot11Elt].info
                ssid=ssid.decode('utf-8','ignore')
                v = manuf.MacParser(update=True)
                ven = v.get_manuf(p.addr2)
                if ssid == "":
                    ssid="gen-probe no SSID"
                    print >> f, strftime("%m/%d/%Y %H:%M:%S - ") + "[%s] - [%s] looking for --> [%s]" %(mac,ven,ssid)
                    print strftime("%m/%d/%Y %H:%M:%S - ") + "[%s] - [%s] looking for --> [%s]" %(mac,ven,ssid)

if broad in no :
    print("Sniffing probe requests only with SSID... (This can take a bit)")
    def proc(p):
        if ( p.haslayer(Dot11ProbeReq) ):
                mac=re.sub('','',p.addr2)
                ssid=p[Dot11Elt].info
                ssid=ssid.decode('utf-8','ignore')
                v = manuf.MacParser(update=True)
                ven = v.get_manuf(p.addr2)
                if ssid == "":
                    sys.stdout.write('')
                else :
                    print >> f, strftime("%m/%d/%Y %H:%M:%S - ") + " [%s] [%s] looking for --> [%s]" %(mac,ven,ssid)
                    print strftime("%m/%d/%Y %H:%M:%S - ") + " [%s] [%s] looking for --> [%s]" %(mac,ven,ssid)
sniff(iface=iname,prn=proc)

if KeyboardInterrupt:
            print("Interrupted. Exiting...")
            f.close()
