#!/usr/bin/env python
"""
This is the script containing all the test code for the ortholotree package.
"""

import unittest
from pkg_resources import resource_filename, resource_exists, resource_stream

from orthomods import internal, external

class TestUnitTest(unittest.TestCase):
    def test_truepasses(self):
        self.assertTrue(True)

    def test_falsepasses(self):
        self.assertFalse(False)

    def test_equalpasses(self):
        self.assertEqual(1,1)
        self.assertEqual('a', 'a')
        self.assertEqual([1,'a'], [1,'a'])

    def test_typeerror(self):
        with self.assertRaises(TypeError):
            " ".split(2)




if __name__ == '__main__':
    unittest.main()