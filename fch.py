#!/usr/bin/python3
#-*-coding:utf-8-*-

import os

findheaderdir = [
	'/usr/include/'
	,'/usr/include/x86_64-linux-gnu/'
]

hd = []

def addhd(txt):
	global hd 
	hd += [txt]

def findhd(txt):
	for d in findheaderdir:
		for h in hd:
			p = os.path.join(d,h)
			if os.path.exists(p):
				with open(p, 'r') as f:
					for l in f.readlines():
						if txt in l:
							print('%s\t%s' % (p, l))

if __name__ == '__main__':
	#test
	addhd('net/ethernet.h')
	findhd('u_int8_t ether')

