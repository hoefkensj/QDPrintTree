#!/usr/bin/env python
# ##############################################################################
# # PROJ: QDPrintTree                    AUTHORS:         Hoefkens.j@gmail.com #
# # FILE: main.py                                                              #
# # REPO: hoefkensj/QDPrintTree.git                                            #
# # HOST: github.com                                                           #
# # VERSION: 0.1.0                                                             #
# # UPDATED: 20230601:013700                                                   #
# ##############################################################################
from QDPrintTree.conf import settings,static
from inspect import getmembers,isbuiltin,isfunction
from shutil import get_terminal_size

class build:
	@staticmethod
	def Node(pfx,key,idx,tot,val,**k):
		def offset(last):
			off=[*pfx]
			if last:	off+=[' ',' ']
			else: 		off+=['{3}',' ']
			return off
		def tree(last,objType):
			lst=[]
			if last:lst+=['{4}']
			else: lst+=['{2}']
			lst+=['{1}']
			if objType in ['dict', 'class','type']: lst+=['{5}']
			else: lst+=['{1}']
			lst+=['{0}']
			return lst
	
		objType  = tools.typeName(val)
		n={ 'pfx':pfx,
			  'idx':idx,
			  'tot':tot,
			  'key':key,
				'charset' : k.get('chars'),
			}
	
		n['val'] = tools.parseVal(val,objType)
		n['type']= objType
		last     = (n['idx']==n['tot'])
		n['off'] = offset(last)
		n['tree']= tree(last, objType)
		return n
	@staticmethod
	def Structure(node,pfx=None,**k):
		chars=k.get('charset',1)
		if type(chars).__name__ == 'int':
			chars=tools.charset(**k)
		b={}
		if not pfx:  pfx=[]
		tot=len(node)
		for idx, key in enumerate(node, start=1):
			n={}
			n=build.Node(pfx,key,idx,tot,node[key],chars=chars,**k)
			if n['type'] in ['dict','type','class','mappingproxy']:
				n['val']=build.Structure(n['val'],pfx,**k)
			
			b[key]=n
		return b
	@staticmethod
	def Tree(node, struct, **k):
		b=struct
		string=''
		for key in b:

			string+='\n'
			string+=tools.mkup(''.join(b[key]['off']), 'tree').format(*b[key]['charset'])
			string+=tools.mkup(''.join(b[key]['tree']), 'tree').format(*b[key]['charset'])
			string+='{K}'
			if b[key]['type'] in ['dict', 'class']:
				string+=tools.mkup(b[key]['key'], b[key]['type'])
				string+='{C}'
				string+=tools.mkup(':')
				string+=build.Tree(b[key]['val'],struct[key]['val'], **k)
			else:
				string+=tools.mkup(b[key]['key'], 'key')
				string+='{C}'
				string+=tools.mkup(':')
				string+='{V}'
				string+=tools.mkup(b[key]['val'], b[key]['type'])
		return string

class tools:
	@staticmethod
	def charset(**k):
		sets = settings.get('charset')
		sel  = k.get('charset', 1)
		return sets[sel]
	@staticmethod
	def typeName(obj):return type(obj).__name__
	@staticmethod
	def parseVal(val,valType):
		if valType in ['type','class','mappingproxy']:
			result=tools.todict(val)
		elif valType in ['function','method']:
			result=f'{val.__name__}()'
		else:
			result=val
		return result
	@staticmethod
	def todict(obj):
		if not isbuiltin(obj):
				if __dict__ in dir(obj):
					result={**obj.__dict__}
				else:
					result={k:getattr(obj,k) for k in dir(obj) }
		return result
	@staticmethod
	def mkup(string,style=''):
		mask=static['stylemask']
		pfx=settings['markup'].get(style,'')
		sfx=settings['markup'].get('reset')
		result=mask.format(PFX=pfx, STR=string, SFX=sfx)
		return  result

def string(**k):
	name=[*k.keys()][0]
	data=k.get(name)
	k.pop(name)
	offset=k.get('offset',['  ','  ','  '])
	K=offset[0]
	C=offset[1]
	V=offset[2]
	treeStruct=build.Structure(data,**k)
	treeString=build.Tree(data,treeStruct,**k)
	return treeString.format(K=K,C=C,V=V)
def stdOut(**k):
	result=string(**k)
	print(result)