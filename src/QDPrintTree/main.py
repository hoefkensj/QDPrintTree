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
def islike(obj):
	state='val'
	if isinstance(obj, dict):
		state='dict'
	if not isbuiltin(obj):
		if '__dict__' in dir(obj):
			state='class'
	if isfunction(obj):
			state='function'
	
	return state
def todict(obj):
	result=obj
	if not isbuiltin(obj):
		if '__dict__' in dir(obj):
			result=obj.__dict__
		if isfunction(obj):
			result=obj.__name__
	return result
	

def mkup(string,style=''):
	mask=static['stylemask']
	pfx=settings['markup'].get(style,'')
	sfx=settings['markup'].get('reset')
	result=mask.format(PFX=pfx, STR=string, SFX=sfx)
	return  result
	
def buildNode(**k):
	def offset(n):
		n['off']+=[' ' if n['set'][0] == n['set'][1] else c[3]]
		n['off']+=' '
		return n
	def tree(n):
		n['tree']=[c[4] if n['set'][0] == n['set'][1] else c[2]]
		n['tree']+=[c[1]]
		n['tree']+=[c[5] if islike(n['val']) in ['dict','class'] else c[1]]
		n['tree']+=[c[0]]
		return n
	n={}
	c=settings.get('styles')[k.get('charset',1)]
	v=k.get('val')
	n['pfx']=k.get('pfx')
	n['off']=[*n['pfx']]
	n['set']=[k.get('idx'), k.get('tot')]
	n['type']= islike(v)
	n['key']=k.get('key')
	n['val']=todict(v)
	n=offset(n)
	n=tree(n)
	return n
def buildTree(node,pfx=None,**k):
	if not pfx:	pfx=[]
	
	string=''
	b={}
	tot=len(node)
	for idx,key in enumerate(node,start=1):
		b[key]=buildNode(
		            pfx=pfx,
		            idx=idx,
		            tot=tot,
		            key=key,
		            val=node[key],
	              **k
		            )

		
	for key in b:
		string+='\n'
		string+=mkup(''.join(b[key]['pfx']))
		string+=mkup(''.join(b[key]['tree']),'tree')
		string+='{K}'
		if b[key]['type'] in ['dict','class']:
			

			string+=mkup(b[key]['key'], b[key]['type'])
			string+='{C}'
			string+=mkup(':')
			string+=buildTree(b[key]['val'],b[key]['off'])
		else:
			
			string+=mkup(b[key]['key'], 'key')
			string+='{C}'
			string+=mkup(':')
			string+='{V}'
			string+=mkup(b[key]['val'],b[key]['type'])
		


	return string


def getPrintTree(**k):
		name=[*k.keys()][0]
		data=k.get(name)
		K=k.get('offset_key',' ')
		C=k.get('offset_colon',' ')
		V=k.get('offset_value',' ')
		treeString=buildTree(data)
		return treeString.format(K=K,C=C,V=V)