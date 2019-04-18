#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sca_trace_route.py
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
#http://www.stashofcode.fr/code/traceroute-roots-en-python-avec-scapy/traceroute.py

from scapy.all import *

def main(args):
	hostname = "www.google.fr"
	limite = 20
	timeout = 20
	host = socket.gethostbyname(hostname)
	print('Traceroute jusqu\'a  {} {} en {} postes maximum, délai de réponse de {} ms...'.format(hostname, host,limite,timeout))
	for i in range(1, limite + 1):
		packet = IP(dst=host, ttl=i)/ICMP(type='echo-request')
		packets = scapy.sendrecv.sr1(packet, verbose=False, timeout=timeout)
		if packets:
			try:
				hostname = socket.gethostbyaddr(packets[0].src)[0]
			except:
				hostname = 'Hôte non trouvé !'
			print('[{}] {} - {}'.format(i, hostname, packets[0].src))
			if packets [0].src == host:
				break
		else:
			print('{} Hors délai !'.format(i))
	print('Traceroute terminé.')
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
