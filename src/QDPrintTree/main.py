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


def txtwrap(string, offset):
	string = shorten(string, 80 - len(offset))
	return string


def pTree(*a, **k):
	d = a[0]
	style = k.get('style', 1)
	offset = [*k.get('offset', '')]
	symb = settings['styles'][style]
	maxw = k.get('max-width', settings.get('maxw', 160))
	keys = [*d.keys()]

	mreset = settings['markup'].get('reset')
	mdict  = settings['markup'].get('dict')
	mfn    = settings['markup'].get('function')
	mkey   = settings['markup'].get('key')
	mval   = settings['markup'].get('val')

	for key in keys:
		koffset = [
			symb[-1],
		]
		coffset = [' ']
		val = d[key]
		if '__dict__' in dir(d[key]):
			val = d[key].__dict__()
		koffset += symb[3 * isinstance(d[key], dict)]
		if key == [*d.keys()][-1]:
			koffset += [symb[2]]
			coffset += [' ']
		else:
			koffset += [symb[1]]
			coffset += [symb[4]]

		print(''.join(offset), symb[0].join(koffset[::-1]), end='')

		if isinstance(d[key], dict):
			print(mdict,end='')
			print(key, end=mreset)
			print('\t:')
			pTree(d[key], offset=[*offset, *coffset], style=style)
		else:
			print(mkey,key,mreset,end='')

			mstr=(mfn * callable(val)) or mval

			print('\t:\t',mstr,shorten(repr(val), maxw),mreset)
