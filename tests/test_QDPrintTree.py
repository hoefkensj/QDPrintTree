#!/usr/bin/env python
# # # PROJECT: QDPrintTree                        AUTHOR: Hoefkens.j@gmail.com
# # FILE: QDPrintTree.py           20230501:014156
# #
import unittest
from src import QDPrintTree

class QDTest(unittest.TestCase):


	def test_ptree(self):
		test_dict={
		'root' : {
								'aaaa':'b',
								'cccc': {
											'dddd': print,
											'ffff': type,
											'hhhh': {
														'i' : 'j'},
											'kkkk':'l'}
			}							}
		QDPrintTree.pTree(test_dict)




if __name__ == '__main__':
	unittest.main()
