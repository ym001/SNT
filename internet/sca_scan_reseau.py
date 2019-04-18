#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sca_scan_reseau.py
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

	# scan sur la plage 192.168.1.1 a 192.168.1.45
	rang = '192.168.1.1-45'
	rep,non_rep = sr( IP(dst=rang) / ICMP() , timeout=0.5 )
	print "-------- Fin Envoi des ping ---------------"
	for elem in rep :
		if elem[1].type == 0 : # 0 <=> echo-reply
			print elem[1].src + ' a renvoye un echo-reply au ping vers ' + str(elem[0].dst)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
