#!/usr/bin/env python
# ##############################################################################
# # PROJ: QDPrintTree                    AUTHORS:         Hoefkens.j@gmail.com #
# # FILE: conf.py                                                              #
# # REPO: hoefkensj/QDPrintTree.git                                            #
# # HOST: github.com                                                           #
# # VERSION: 0.1.0                                                             #
# # UPDATED: 20230601:013700                                                   #
# ##############################################################################

settings = {
	'styles': [
		['-', '+', '+', '+', '|', '<'],
		['─', '├', '└', '┬', '│', '╸'],
		['━', '┣', '┗', '┳', '┃', '╾╸ '],
		['═', '╠', '╚', '╦', '║', '╾╸ '],
	],
	'maxw': 160,
	'markup' : {
		'reset'     : '\x1b[m',
		'dict'      : '\x1b[1;34m',
		'function'  : '\x1b[35m',
		'key'       : '\x1b[0;39m',
		'val'				:	'\x1b[0;33m'
	}
}
