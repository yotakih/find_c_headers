#!/usr/bin/python3
#-*-coding:utf-8-*-

import os
import sys

def find(txt):
	print('--------find result--------')
	for r,d,fs in os.walk('/usr/include/'):
		for f in fs:
			if os.path.splitext(f)[1] == '.h':
				p = os.path.join(r,f)
				with open(p) as f:
					for l in f.readlines():
						if txt in l:
							print('%s\t%s' % (p, l))

def main():
	if len(sys.argv) < 2:
		print('error args. please select find works!!')
		sys.exit()
	find(sys.argv[1])

if __name__ == '__main__':
	main()

