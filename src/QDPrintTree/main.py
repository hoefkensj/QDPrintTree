#!/usr/bin/env python
# # # PROJECT: QDPrintTree                        AUTHOR: Hoefkens.j@gmail.com
# # FILE: main.py           20230501:013700
# #


#!/usr/bin/env python
from textwrap import shorten
from conf import settings



def txtwrap(string,offset):
	string=shorten(	string, 80-len(offset))
	return string

def pTree(*a, **k):
	d = a[0]
	style=k.get('style',1)
	offset=[*k.get('offset', '')]
	symb=settings['styles'][style]
	maxw=k.get('max-width',settings.get('maxw',160))
	keys=[*d.keys()]
	for key in keys:
		koffset=[symb[-1],]
		coffset=[' ']
		val=d[key]
		if '__dict__' in dir(d[key]):
			val=d[key].__dict__()
		koffset+=symb[3 * isinstance(d[key],dict)]
		if key == [*d.keys()][-1]:
			koffset+=[symb[2]]
			coffset+=[' ']
		else:
			koffset+=[symb[1]]
			coffset+=[symb[4]]

		print(''.join(offset),symb[0].join(koffset[::-1]),end='')
		print(key,end='')
		if isinstance(d[key],dict):
			print('\t:')
			pTree(d[key],offset=[*offset,*coffset],style=style)
		else:
			print('\t:\t',shorten(repr(val),maxw))




test_dict={
		'root' : {
								'aaaa':'b',
								'cccc': {
											'dddd': 'e',
											'ffff': 'g',
											'hhhh': {
														'i' : 'j'},
											'kkkk':'l'},
							}
}
pTree(test_dict,style=1)
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