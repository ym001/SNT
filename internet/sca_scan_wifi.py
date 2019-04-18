#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sca_scan_wifi.py
#  
#  Copyright 2019 Mercadier <mercadier@mercadier>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from scapy.all import *
def packetRecup (pkt) :
    if pkt.haslayer (Dot11) :
        if pkt.type == 0 and pkt.subtype == 8 :
            if pkt.addr2 not in ap_list :
                ap_list.append(pkt.addr2)
                return "Réseau SSID: %s et MAC address: %s " %(pkt.info, pkt.addr2)

def main(args):
	
	ap_list = []
	carte_wifi=""
	sniff(iface = carte_wifi , prn = packetRecup)

	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
