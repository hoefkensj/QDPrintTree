#!/usr/bin/env python
# ##############################################################################
# # PROJ: QDPrintTree                    AUTHORS:         Hoefkens.j@gmail.com #
# # FILE: conf.py                                                              #
# # REPO: hoefkensj/QDPrintTree.git                                            #
# # HOST: github.com                                                           #
# # VERSION: 0.1.0                                                             #
# # UPDATED: 20230601:013700                                                   #
# ##############################################################################
static={
	'stylemask' : '{PFX}{STR}{SFX}'
	}

settings = {
	'styles': [
		['\\' ,'-','+', '',  '+', '+',      ],
		['╸' ,'─','├', '│',  '└', '┬',  '┍' ],
		['╾╸','━','┣', '┃',  '┗', '┳',      ],
		['╾╸','═','╠', '║',  '╚', '╦',      ],
	],
	'maxw': 160,
	'markup' : {
		'reset'     : '\x1b[m',
		'tree'      : '\x1b[0;29m',
		'dict'      : '\x1b[1;34m',
		'class'     : '\x1b[1;31m',
		'function'  : '\x1b[35m',
		'key'       : '\x1b[0;33m',
		'val'				:	'\x1b[0;37m'
	}
}