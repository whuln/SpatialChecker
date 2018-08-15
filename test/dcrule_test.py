#_*_ coding: UTF-8 _*_

import unittest

import const
from datacheck import DataCheckRules

rulelist = [
    ['SPCTRLP', u'测量控制点', [110101, 110102, 110103, 110201, 110202, 110301, 110302, 110401, 110402]],
    ['SPGRIDL', u'坐标格网', [120200]]
]

dcr = DataCheckRules(rulelist)

class dcruleteset(unittest.TestCase):


    def test_const(self):
        self.assertEqual(const.fc_name, 0)
        self.assertEqual(const.fc_aliasname, 1)
        self.assertEqual(const.fc_fcode, 2)


    def test_getfcnames(self):
        print dcr.getfcnames()

    def test_getfcaliasnames(self):
        print 'fcaliasnames'
        print dcr.getfcaliasnames()

    def test_getfcodeoffc(self):
        print 'fcode'
        print dcr.getfcode_of_fc('SPCTRLP')


if __name__ == '__main__':
    unittest.main()