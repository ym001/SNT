#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sca_trame.py
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

def main(args):
	#paquet IP
	
	packet = IP()
	packet.ttl = 42
	print "Envoie d'un paquet IP avec TTL = 42 "

	packet.show()
	
	#trame etherhet
	print "Envoie d'une trame éthernet: "

	ma_trame = Ether()
	print(ma_trame.show())
	sendp(ma_trame)
	
	# creation du paquet IP a destination de www.google.fr, ce paquet IP contenant un ICMP
	mon_ping_google=Ether()/IP(dst='www.google.fr')/ICMP()
	rep,non_rep = srp(mon_ping_google)
	print(rep.show())
	# Affichage de ce paquet : affiche son contenu Ethernet, IP et ICMP
	print "Envoie d'un paquet icmp vers google : "
	mon_ping_google.show()
	


	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
