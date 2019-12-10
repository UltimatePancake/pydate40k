# -*- coding: utf-8 -*-

import unittest

from pydate40k.Date40k import Date40k


class TestDate40k(unittest.TestCase):
    def test_parse_good_date(self):
        result = Date40k("1999-05-11 13:00:00")
        self.assertEqual(str(result), "360 999.M2")

    def test_parse_bad_date(self):
        result = Date40k("1999-05-11 13")
        self.assertNotEqual(str(result), "360 999.M2")


if __name__ == '__main__':
    unittest.main()
