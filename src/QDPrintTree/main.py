#!/usr/bin/env python
# ##############################################################################
# # PROJ: QDPrintTree                    AUTHORS:         Hoefkens.j@gmail.com #
# # FILE: main.py                                                              #
# # REPO: hoefkensj/QDPrintTree.git                                            #
# # HOST: github.com                                                           #
# # VERSION: 0.1.0                                                             #
# # UPDATED:  20230501:013700                                                  #
# ##############################################################################
#
from textwrap import shorten
from QDPrintTree.conf import settings


def txtwrap(string, max,offset):
	string = shorten(string, max - len(offset))
	return string


def pTree(*a, **k):
	d      = a[0]
	style  = k.get('style', 1)
	offset = [*k.get('offset', '')]
	# coll	 = k.get('collapse', ['dunder',])  																		TODO
	maxw   = k.get('max-width', settings.get('maxw', 160))
	symb   = settings['styles'][style]
	mreset = settings['markup'].get('reset')
	mdict  = settings['markup'].get('dict')
	mfn    = settings['markup'].get('function')
	mkey   = settings['markup'].get('key')
	mval   = settings['markup'].get('val')

	for key in d:
		koffset=[symb[-1]]
		coffset=[' ']
		val=d[key]
		if '__dict__' in dir(val):
			val=dict(val.__dict__)
		koffset+=symb[3 * isinstance(val, dict)]
		koffset+=[symb[1]]
		coffset+=[symb[4]]
		if key == [*d.keys()][-1]:
			koffset[-1]=symb[2]
			coffset[-1]=' '
		print(''.join(offset), symb[0].join(koffset[::-1]), end='')

		if isinstance(val, dict):
			print(mdict,key,mreset,':')
			pTree(val, offset=[*offset, *coffset], style=style)
		else:
			print(mkey, key, mreset, end='')
			mstr=(mfn * callable(val)) or mval
			print('\x1b[40G:\t', mstr, txtwrap(repr(val), maxw,coffset), mreset)
