#!/usr/bin/env python
# # # PROJECT: QDPrintTree                        AUTHOR: Hoefkens.j@gmail.com
# # FILE: QDPrintTree.py           20230501:014156
# #
import unittest
import QDPrintTree
def testfunction():
		pass
class QDTest(unittest.TestCase):


	def test_ptree(self):
		test_dict={
		'root' : {
								'key[1,0]':'val[1,0]',
								'key[1,1]': {
											'key[2,0]': 'val[2,0]',
											'key[2,1]': type,
											'key[2,2': {
														'key[3,0]' : 'val[3,0]'},
											'kkkk': testfunction }
			}							}
		print(QDPrintTree.getPrintTree(test=test_dict,style=1))




if __name__ == '__main__':
	unittest.main()