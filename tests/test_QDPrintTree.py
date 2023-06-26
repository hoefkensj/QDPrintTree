#!/usr/bin/env python
# # # PROJECT: QDPrintTree                        AUTHOR: Hoefkens.j@gmail.com
# # FILE: QDPrintTree.py           20230501:014156
# #
import unittest
import QDPrintTree
def tstfunction():
		pass
class tstClass:
	def __init__(slf,*a,**k):
		slf.a=a
		slf.k=k
class QDTest(unittest.TestCase):


	def test_ptree(self):
		tstInstance=tstClass('argument',test='ikkel')
		test_dict={
		'root' : {
								'key[1,0]':'val[1,0]',
								'key[1,1]': {
											'key[2,0]': 'val[2,0]',
											'key[2,1]': tstInstance,
											'key[2,2': {
														'key[3,0]' : 'val[3,0]'},
											'kkkk': tstfunction }
			}							}
		print(QDPrintTree.string(test=test_dict))
		print(QDPrintTree.string(test=test_dict,charset=0))
		QDPrintTree.stdOut(test=test_dict,charset=2)




if __name__ == '__main__':
	unittest.main()