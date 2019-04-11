#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  requette.py
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


def main(args):
	import requests
	url="https://github.com/ym001/SNT"

	#proxy = {"http":"http://username:password@proxy:port"}
	#r = requests.get(url, proxies = proxy)
	r = requests.get(url)
	print(r.text)
	#r = requests.put(url)
    #r = requests.delete(url)
    #r = requests.patch(url)
    #r = requests.post(url)
    #r = requests.head(url)
    #r = requests.options("http://linuxfr.org/")
    
    #envoyer des données
	data = {"first_name":"Richard", "second_name":"Stallman"}
	r = requests.post(url, data = data)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
