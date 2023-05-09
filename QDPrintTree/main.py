#!/usr/bin/env python
# # # PROJECT: QDPrintTree                        AUTHOR: Hoefkens.j@gmail.com
# # FILE: main.py           20230501:013700
# #


#!/usr/bin/env python
import sys
from textwrap import shorten


def hasDict(d):
	return any([True for key in d if isinstance(d[key], dict)])


def overview(d):
	sys.stdout.write(
		f"(\x1b[1;33m{(sd:=len([item for item in d if isinstance(d[item],dict)]))}\x1b[0m Groups +\x1b[1;31m {len(d) - sd}\x1b[0m items)"
		+ "\x1b[0m"
	)


def pTree(*a, **k):
	d = a[0]
	maxd = a[1] if len(a) > 1 else 0
	limi = k.get("limit") or (a[2] if len(a) > 2 else 0)
	offset=k.get('offset', '')
	depth = k.get("depth") or 0
	keys = len(d.keys())

	depthstop = True if (maxd == depth and not maxd <= 0) else False
	limstop = True if (len(d) >= limi and not limi <= 0) else False
	# print(depthstop,maxd,depth)
	# print(limstop,limi,keys)

	if limstop or depthstop:
		overview(d)
	else:
		for key in d:
			dkey = shorten(
				f"\x1b[32m{d[key]}\x1b[0m" if callable(d[key]) else str(d[key]), 40
			)

			keys -= 1


			if isinstance(d[key], dict):
				sys.stdout.write("\n")
				sys.stdout.write(offset)
				sys.stdout.write("  ┗━━ " if keys == 0 else "  ┣━━ ")
				sys.stdout.write(f"\x1b[1;34m{str(key)}\t:\x1b[0m\t")
				if keys ==0 :
					offset+="     "
				else :
					offset+="  ┃  "
				pTree(d[key], maxd, limi, depth=depth + 1,offset=offset)
			else:
				sys.stdout.write("\n")
				sys.stdout.write(offset)
				sys.stdout.write("  ┗━━ " if keys == 0 else "  ┣━━ ")
				sys.stdout.write(f"{str(key)}\t:\t{dkey}")
			offset=offset[:-6]
test_dict={
						'a':'b',
						'c': {
									'd': 'e',
									'f': 'g',
									'h': {
												'i' : 'j',
												'k':'l',
												},
									'm':'n'}
						}
pTree(test_dict)

'''
test_dict:
	├──╸a:  b
	└─┬╸c:
		├───╸d:  e
		├───╸f:  g
		├─┬─╸h:
		│ ├───╸i:  j
		│ └───╸k:  l
		└───╸m:  n
'''