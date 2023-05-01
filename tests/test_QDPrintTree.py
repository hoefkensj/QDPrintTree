#!/usr/bin/env python
# # # PROJECT: QDPrintTree                        AUTHOR: Hoefkens.j@gmail.com
# # FILE: QDPrintTree.py           20230501:014156
# #
import unittest
import QDPrintTree

class MyTestCase(unittest.TestCase):
	# def test_something(self):
	# 	self.assertEqual(True, False)  # add assertion here

	def test_ptree(self):
		test_dict={
								'a':'b',
								'c': {
											'd': 'e',
											'f': 'g',
											'h': {
														'i' : 'j'},
											'k':'l'}
 								}
		QDPrintTree.pTree(test_dict)
		# element=QElement('Qid','QType')
		# self.assertEqual(element.Meta.QId, 'Qid')



if __name__ == '__main__':
	unittest.main()
