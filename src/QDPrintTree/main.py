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
	d      = a[0]
	style  = k.get('style', 1)
	offset = [*k.get('offset', '')]
	coll	 = k.get('collapse', ['dunder',])
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
			print(mdict, end='')
			print(key, end=mreset)
			print(':',end='')
			pTree(val, offset=[*offset, *coffset], style=style)
		else:
			print(mkey, key, mreset, end='')
			mstr=(mfn * callable(val)) or mval
			print('\x1b[40G:\t', mstr, shorten(repr(val), maxw), mreset)


# #!/usr/bin/env python
# # ##############################################################################
# # # PROJ: QDPrintTree                    AUTHORS:         Hoefkens.j@gmail.com #
# # # FILE: main.py                                                              #
# # # REPO: hoefkensj/QDPrintTree.git                                            #
# # # HOST: github.com                                                           #
# # # VERSION: 0.1.0                                                             #
# # # UPDATED:  20230501:013700                                                  #
# # ##############################################################################
# #
# from textwrap import shorten
# from QDPrintTree.conf import settings
#
#
# # def txtwrap(string, offset):
# # 	string = shorten(string, 80 - len(offset))
# # 	return string
# # def collapse_dunder(obj):
# # 	dunders=[i for i in dir(obj) if i.startswith('__')]
# # 	n=len(dunders)
# # 	cstr=f' ... + {n} dunder methods hidden'
# # 	new=[cstr,[i for i in dir(obj) if i not in dunders ]]
# # 	return new
# #
# # def buffer(*str,**k):
# # 	end=k.get('end')
# # 	sep=k.get('sep')
# # 	return f'{sep}'.join([*str,end])
#
#
# def pTree(*a, **k):
# 	d      = a[0]
# 	style  = k.get('style', 1)
# 	offset = [*k.get('offset', '')]
# 	coll	 = k.get('collapse', ['dunder',])
# 	maxw   = k.get('max-width', settings.get('maxw', 160))
# 	symb   = settings['styles'][style]
# 	mreset = settings['markup'].get('reset')
# 	mdict  = settings['markup'].get('dict')
# 	mfn    = settings['markup'].get('function')
# 	mkey   = settings['markup'].get('key')
# 	mval   = settings['markup'].get('val')
#
# 	for key in d:
# 		koffset=[symb[-1]]
# 		coffset=[' ']
#
# 		val=d[key]
# 		if '__dict__' in dir(val):
# 			val=dict(val.__dict__)
# 			val=collapse_dunder(val)
# 		koffset+=symb[3 * isinstance(val, dict)]
# 		koffset+=[symb[1]]
# 		coffset+=[symb[4]]
# 		if key == [*d.keys()][-1]:
# 			koffset+=[symb[2]]
# 			coffset+=[' ']
# 		print(''.join(offset), symb[0].join(koffset[::-1]), end='')
# 		# stdout=buffer(''.join(offset), symb[0].join(koffset[::-1]), end='')
#
# 		if isinstance(val, dict):
# 			print(mdict, end='')
# 			print(key, end=mreset)
# 			print('\t:')
# 			pTree(val, offset=[*offset, *coffset], style=style)
# 		else:
# 			print(mkey, key, mreset, end='')
# 			mstr=(mfn * callable(val)) or mval
# 			print('\t:\t', mstr, shorten(repr(val), maxw), mreset)

